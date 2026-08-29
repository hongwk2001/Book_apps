package com.tkprof.shared.billing

import android.app.Activity
import android.content.Context
import com.android.billingclient.api.*
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow

/**
 * Manages Google Play Billing for per-book in-app purchases.
 * Each book app passes its own iapProductId (e.g. "com.tkprof.dracula.full").
 */
class BillingManager(
    private val context: Context,
    private val tipProductIds: List<String>
) {

    private val _isFullUnlocked = MutableStateFlow(false)
    val isFullUnlocked: StateFlow<Boolean> = _isFullUnlocked

    private val _isConnected = MutableStateFlow(false)
    val isConnected: StateFlow<Boolean> = _isConnected

    private lateinit var billingClient: BillingClient

    private val purchasesUpdatedListener = PurchasesUpdatedListener { result, purchases ->
        if (result.responseCode == BillingClient.BillingResponseCode.OK && purchases != null) {
            purchases.forEach { handlePurchase(it) }
        }
    }

    fun init() {
        billingClient = BillingClient.newBuilder(context)
            .setListener(purchasesUpdatedListener)
            .enablePendingPurchases(
                PendingPurchasesParams.newBuilder().enableOneTimeProducts().build()
            )
            .build()

        billingClient.startConnection(object : BillingClientStateListener {
            override fun onBillingSetupFinished(result: BillingResult) {
                if (result.responseCode == BillingClient.BillingResponseCode.OK) {
                    _isConnected.value = true
                    restorePurchases()
                }
            }
            override fun onBillingServiceDisconnected() {
                _isConnected.value = false
            }
        })
    }

    private fun restorePurchases() {
        billingClient.queryPurchasesAsync(
            QueryPurchasesParams.newBuilder()
                .setProductType(BillingClient.ProductType.INAPP)
                .build()
        ) { _, purchases ->
            val unlocked = purchases.any { p ->
                p.purchaseState == Purchase.PurchaseState.PURCHASED &&
                p.products.any { it in tipProductIds }
            }
            _isFullUnlocked.value = unlocked
            purchases.filter { !it.isAcknowledged }.forEach { acknowledgePurchase(it) }
        }
    }

    private fun handlePurchase(purchase: Purchase) {
        if (purchase.purchaseState == Purchase.PurchaseState.PURCHASED &&
            purchase.products.any { it in tipProductIds }) {
            _isFullUnlocked.value = true
            if (!purchase.isAcknowledged) acknowledgePurchase(purchase)
        }
    }

    private fun acknowledgePurchase(purchase: Purchase) {
        val params = AcknowledgePurchaseParams.newBuilder()
            .setPurchaseToken(purchase.purchaseToken)
            .build()
        billingClient.acknowledgePurchase(params) { /* log result */ }
    }

    /**
     * Launch the Google Play purchase flow.
     * @param activity Current Activity (required by Play Billing API)
     */
    fun launchPurchaseFlow(activity: Activity, productId: String) {
        val productList = listOf(
            QueryProductDetailsParams.Product.newBuilder()
                .setProductId(productId)
                .setProductType(BillingClient.ProductType.INAPP)
                .build()
        )
        billingClient.queryProductDetailsAsync(
            QueryProductDetailsParams.newBuilder().setProductList(productList).build()
        ) { result, queryProductDetailsResult ->
            android.os.Handler(android.os.Looper.getMainLooper()).post {
                if (result.responseCode == BillingClient.BillingResponseCode.OK) {
                    val productDetailsList = queryProductDetailsResult.productDetailsList
                    if (productDetailsList.isNotEmpty()) {
                        val flowParams = BillingFlowParams.newBuilder()
                            .setProductDetailsParamsList(
                                listOf(
                                    BillingFlowParams.ProductDetailsParams.newBuilder()
                                        .setProductDetails(productDetailsList.first())
                                        .build()
                                )
                            )
                            .build()
                        billingClient.launchBillingFlow(activity, flowParams)
                    } else {
                        android.widget.Toast.makeText(activity, "Product ID not found: $productId", android.widget.Toast.LENGTH_LONG).show()
                    }
                } else {
                    android.widget.Toast.makeText(activity, "Billing Error: " + result.debugMessage, android.widget.Toast.LENGTH_LONG).show()
                }
            }
        }
    }

    fun disconnect() {
        if (::billingClient.isInitialized) billingClient.endConnection()
    }
}
