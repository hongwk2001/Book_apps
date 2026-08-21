import re

with open(r'C:\git_repo\Book_apps\shared\src\main\java\com\tkprof\shared\ui\reader\ReaderViewModel.kt', 'r', encoding='utf-8') as f:
    text = f.read()

prefs_decl = '''
    private val prefs = application.getSharedPreferences("ReaderPrefs", Context.MODE_PRIVATE)
'''
text = re.sub(r'private val repository = BookRepository\(application\)', r'private val repository = BookRepository(application)\n' + prefs_decl, text)

# update loadChapter
old_load = '''    fun loadChapter(number: Int) {
        viewModelScope.launch(Dispatchers.IO) {
            ttsManager.stop()
            _speakingSentenceId.value = null
            currentQueueIndex = -1
            _currentChapterNumber.value = number
            val ch = repository.loadChapter(number)
            _currentChapter.value = ch
            rebuildSentenceQueue(ch)
        }
    }'''

new_load = '''    fun loadChapter(number: Int, restoreSentenceId: String? = null) {
        prefs.edit().putInt("last_chapter", number).apply()
        viewModelScope.launch(Dispatchers.IO) {
            ttsManager.stop()
            _speakingSentenceId.value = null
            currentQueueIndex = -1
            _currentChapterNumber.value = number
            val ch = repository.loadChapter(number)
            _currentChapter.value = ch
            rebuildSentenceQueue(ch)
            
            if (restoreSentenceId != null) {
                val idx = sentenceQueue.indexOfFirst { it.id == restoreSentenceId }
                if (idx != -1) {
                    currentQueueIndex = idx
                    _speakingSentenceId.value = restoreSentenceId
                    _speakingParagraphIndex.value = ch?.paragraphs?.indexOfFirst { it.id == sentenceQueue[idx].paragraphId } ?: -1
                }
            } else {
                prefs.edit().remove("last_sentence_id").apply()
            }
        }
    }'''

text = text.replace(old_load, new_load)

init_replacement = '''    init {
        val lastChapter = prefs.getInt("last_chapter", 1)
        val lastSentenceId = prefs.getString("last_sentence_id", null)
        loadChapter(lastChapter, lastSentenceId)
        
        viewModelScope.launch { _totalChapters.value = repository.availableChapterCount() }
        
        // Listen to TTS state to start/stop the foreground service
        viewModelScope.launch {
            isSpeaking.collect { speaking ->
                val intent = Intent(application, TtsPlaybackService::class.java)
                if (speaking) {
                    intent.putExtra("BOOK_TITLE", bookConfig.titleEn)
                    ContextCompat.startForegroundService(application, intent)
                } else {
                    application.stopService(intent)
                }
            }
        }
        
        // Auto-save sentence progress
        viewModelScope.launch {
            speakingSentenceId.collect { id ->
                if (id != null) {
                    prefs.edit().putString("last_sentence_id", id).apply()
                }
            }
        }
    }'''

text = re.sub(r'    init \{\s*loadChapter\(1\)\s*viewModelScope\.launch \{ _totalChapters\.value = repository\.availableChapterCount\(\) \}\s*// Listen to TTS state to start/stop the foreground service\s*viewModelScope\.launch \{\s*isSpeaking\.collect \{ speaking ->\s*val intent = Intent\(application, TtsPlaybackService::class\.java\)\s*if \(speaking\) \{\s*intent\.putExtra\("BOOK_TITLE", bookConfig\.titleEn\)\s*ContextCompat\.startForegroundService\(application, intent\)\s*\} else \{\s*application\.stopService\(intent\)\s*\}\s*\}\s*\}\s*\}', init_replacement, text)


with open(r'C:\git_repo\Book_apps\shared\src\main\java\com\tkprof\shared\ui\reader\ReaderViewModel.kt', 'w', encoding='utf-8') as f:
    f.write(text)
