import re

with open(r'C:\git_repo\Book_apps\shared\src\main\java\com\tkprof\shared\billing\BillingManager.kt', 'r', encoding='utf-8') as f:
    text = f.read()

old_query = '''        billingClient.queryProductDetailsAsync(
            QueryProductDetailsParams.newBuilder().setProductList(productList).build()
        ) { result, productDetailsList ->
            if (result.responseCode == BillingClient.BillingResponseCode.OK &&
                productDetailsList.isNotEmpty()) {
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
            }
        }'''

new_query = '''        billingClient.queryProductDetailsAsync(
            QueryProductDetailsParams.newBuilder().setProductList(productList).build()
        ) { result, productDetailsList ->
            android.os.Handler(android.os.Looper.getMainLooper()).post {
                if (result.responseCode == BillingClient.BillingResponseCode.OK) {
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
                        android.widget.Toast.makeText(activity, "Product ID not found: " + iapProductId, android.widget.Toast.LENGTH_LONG).show()
                    }
                } else {
                    android.widget.Toast.makeText(activity, "Billing Error: " + result.debugMessage, android.widget.Toast.LENGTH_LONG).show()
                }
            }
        }'''

text = text.replace(old_query, new_query)

with open(r'C:\git_repo\Book_apps\shared\src\main\java\com\tkprof\shared\billing\BillingManager.kt', 'w', encoding='utf-8') as f:
    f.write(text)
