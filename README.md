# TKProf Dracula Bilingual Reader

An immersive, bilingual reading application built for Android. This app allows users to read Bram Stoker's Dracula in English with full Korean localization, seamlessly combining standard reading with Text-to-Speech (TTS) capabilities.

## ?? Features

*   **Bilingual Reading Interface:** Read paragraphs with full translation support.
*   **Text-to-Speech (TTS) Integration:**
    *   Listen to the book via Android's native TTS engine.
    *   Adjustable playback speeds (up to 3.0x).
    *   Synchronized auto-scrolling to keep your place while listening.
*   **Audio Focus Management:**
    *   Automatically pauses TTS playback during incoming phone calls or other transient audio interruptions.
    *   Seamlessly resumes playback when audio focus is regained.
*   **Modern Android UI:**
    *   Built entirely with **Jetpack Compose** and Material 3.
    *   Supports both Light and Dark mode reading.
*   **Freemium Architecture:**
    *   Chapters 1-2 are free.
    *   Chapter 3+ locked behind a paywall (ready for billing integration).
*   **Full Korean Localization:**
    *   All UI strings, settings, and menus are fully translated into Korean (alues-ko/strings.xml).
*   **Custom Adaptive Branding:**
    *   Features the official TKProf Deep Purple (#130319) brand color.
    *   Custom edge-to-edge adaptive launcher icons.

## ?? Architecture

This project is built using a modern multi-module architecture:
*   dracula/: The main application module containing book-specific assets and the MainActivity.
*   shared/: A reusable Android library module containing all core logic, TTS Services, Compose UI components (ReaderScreen, SettingsDialog), and ViewModels. This allows rapid deployment of future books by simply swapping the dracula module.

## ?? Tech Stack

*   **Language:** Kotlin
*   **UI Toolkit:** Jetpack Compose
*   **Architecture:** MVVM (Model-View-ViewModel)
*   **Background Processing:** Android Foreground Services (TtsPlaybackService)
*   **Audio:** AudioManager (AudioFocus API)
*   **Build System:** Gradle (Kotlin DSL)

## ?? Getting Started

1.  Clone this repository.
2.  Open the project in **Android Studio (Giraffe or newer)**.
3.  Sync Gradle.
4.  Run the dracula run configuration on an emulator or physical device running Android 8.0 (API 26) or higher.

## ?? License
Copyright TKProf. All rights reserved.
