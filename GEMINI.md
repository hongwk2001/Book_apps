# Build Rules
- Do not build Android release bundles (.aab) or APKs automatically using Gradle. 
- The AI does not have access to the actual production keystore passwords. 
- Instead of building, provide the user with the correct terminal commands (e.g., `./gradlew bundleRelease`) so they can build the release artifacts themselves.
