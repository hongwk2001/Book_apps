plugins {
    alias(libs.plugins.android.application)
    alias(libs.plugins.compose.compiler)
    alias(libs.plugins.kotlin.serialization)
}
android {
    signingConfigs {
        create("release") {
            storeFile = file("C:\\git_repo\\androidkeystore_dracula.jks")
            storePassword = "hongari1"
            keyAlias = "key0"
            keyPassword = "hongari1"
        }
    }
    buildTypes {
        debug {
            // Add this line so your USB builds use the official signature!
            signingConfig = signingConfigs.getByName("release")
        }
    }
    namespace = "com.tkprof.secretgarden"
    compileSdk = 36

    defaultConfig {
        applicationId = "com.tkprof.secretgarden"
        minSdk = 24
        targetSdk = 36
        versionCode = 1
        versionName = "1.0"
    }

    buildTypes {
        release {
            isMinifyEnabled = true
            proguardFiles(
                getDefaultProguardFile("proguard-android-optimize.txt"),
                "proguard-rules.pro"
            )
        }
    }
    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_17
        targetCompatibility = JavaVersion.VERSION_17
    }
    buildFeatures {
        compose = true
    }
    packaging {
        resources {
            excludes += "/META-INF/{AL2.0,LGPL2.1}"
        }
    }
}

kotlin {
    jvmToolchain(17)
}

dependencies {
    implementation(project(":shared"))

    val composeBom = platform(libs.androidx.compose.bom)
    implementation(composeBom)
    implementation(libs.androidx.core.ktx)
    implementation(libs.androidx.lifecycle.runtime.ktx)
    implementation(libs.androidx.activity.compose)
    implementation(libs.androidx.compose.ui)
    implementation(libs.androidx.compose.material3)
    implementation(libs.billing)

    debugImplementation(libs.androidx.compose.ui.tooling)
}

