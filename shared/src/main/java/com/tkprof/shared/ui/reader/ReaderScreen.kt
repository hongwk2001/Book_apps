package com.tkprof.shared.ui.reader

import android.app.Activity
import androidx.compose.ui.res.stringResource
import com.tkprof.shared.R

import android.content.Intent
import android.net.Uri
import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import android.content.ActivityNotFoundException
import androidx.compose.foundation.lazy.rememberLazyListState
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.text.ClickableText
import androidx.compose.foundation.verticalScroll
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.automirrored.filled.ArrowBack
import androidx.compose.material.icons.automirrored.filled.ArrowForward
import androidx.compose.material.icons.filled.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.text.AnnotatedString
import androidx.compose.ui.text.SpanStyle
import androidx.compose.ui.text.buildAnnotatedString
import androidx.compose.ui.text.font.FontStyle
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.tkprof.shared.model.BilingualParagraph
import com.tkprof.shared.model.Language
import com.tkprof.shared.model.Sentence
import com.tkprof.shared.model.SentenceSplitter
import com.tkprof.shared.ui.settings.SettingsDialog
import kotlinx.coroutines.launch

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun ReaderScreen(viewModel: ReaderViewModel) {
    val chapter by viewModel.currentChapter.collectAsState()
    val chapterNumber by viewModel.currentChapterNumber.collectAsState()
    val totalChapters by viewModel.totalChapters.collectAsState()
    val speakingId by viewModel.speakingSentenceId.collectAsState()
    val isSpeaking by viewModel.isSpeaking.collectAsState()
    val isFullUnlocked by viewModel.isFullUnlocked.collectAsState()
    val isEnFirst by viewModel.isEnFirst.collectAsState()
    val showEn by viewModel.showEn.collectAsState()
    val showKo by viewModel.showKo.collectAsState()
    val isAccessible = viewModel.isChapterAccessible(chapterNumber)
    val activity = LocalContext.current as Activity

    var showSettings by remember { mutableStateOf(false) }
    
    val drawerState = rememberDrawerState(initialValue = DrawerValue.Closed)
    val scope = rememberCoroutineScope()

    if (showSettings) {
        SettingsDialog(
            viewModel = viewModel,
            onDismiss = { showSettings = false }
        )
    }

    ModalNavigationDrawer(
        drawerState = drawerState,
        drawerContent = {
            ModalDrawerSheet {
                Column(modifier = Modifier.fillMaxHeight()) {
                    Text(stringResource(R.string.chapters_title), modifier = Modifier.padding(16.dp), style = MaterialTheme.typography.titleLarge)
                    HorizontalDivider()
                    LazyColumn(modifier = Modifier.weight(1f)) {
                        items(totalChapters) { index ->
                            val i = index + 1
                            NavigationDrawerItem(
                                label = { Text(stringResource(R.string.chapter_label, i)) },
                                selected = i == chapterNumber,
                                onClick = { 
                                    viewModel.loadChapter(i)
                                    scope.launch { drawerState.close() }
                                },
                                modifier = Modifier.padding(horizontal = 12.dp, vertical = 2.dp)
                            )
                        }
                    }
                    HorizontalDivider()
                    Column(modifier = Modifier.padding(16.dp)) {
                        Text(stringResource(R.string.about_title), style = MaterialTheme.typography.titleMedium)
                        Spacer(modifier = Modifier.height(8.dp))
                        Text("${stringResource(R.string.version_label)}\n${stringResource(R.string.contact_label)}", style = MaterialTheme.typography.bodySmall)
                        Spacer(modifier = Modifier.height(16.dp))
                        Button(
                            onClick = {
                                try {
                                    activity.startActivity(Intent(Intent.ACTION_VIEW, Uri.parse("market://search?q=pub:TKProf+LLC")))
                                } catch(e: ActivityNotFoundException) {
                                    activity.startActivity(Intent(Intent.ACTION_VIEW, Uri.parse("https://play.google.com/store/apps/developer?id=TKProf+LLC")))
                                }
                            },
                            modifier = Modifier.fillMaxWidth()
                        ) {
                            Text(stringResource(R.string.more_books_btn))
                        }
                    }
                }
            }
        }
    ) {
        Scaffold(
            topBar = {
                TopAppBar(
                    title = {
                        Column {
                            Text(text = viewModel.bookConfig.titleEn, style = MaterialTheme.typography.titleMedium)
                            Text(text = "Chapter $chapterNumber / $totalChapters", style = MaterialTheme.typography.bodySmall, color = MaterialTheme.colorScheme.onSurfaceVariant)
                        }
                    },
                    navigationIcon = {
                        IconButton(onClick = { scope.launch { drawerState.open() } }) {
                            Icon(Icons.Default.Menu, contentDescription = "Menu")
                        }
                    },
                    actions = {
                        IconButton(onClick = { showSettings = true }) {
                            Icon(Icons.Default.Settings, contentDescription = "Settings")
                        }
                    },
                    colors = TopAppBarDefaults.topAppBarColors(containerColor = MaterialTheme.colorScheme.primaryContainer)
                )
            },
            bottomBar = {
                ReaderBottomBar(
                    isSpeaking = isSpeaking,
                    isAccessible = isAccessible,
                    onPrevious = { viewModel.previousSentence() },
                    onNext = { viewModel.nextSentence() },
                    onPlayPause = { viewModel.playOrPause() }
                )
            }
        ) { padding ->
                    val listState = rememberLazyListState()
                    val speakingParagraphIndex by viewModel.speakingParagraphIndex.collectAsState()
                    
                    LaunchedEffect(speakingParagraphIndex) {
                        if (speakingParagraphIndex >= 0) {
                            listState.animateScrollToItem(speakingParagraphIndex)
                        }
                    }

                    if (!isAccessible) {
                PaywallScreen(chapterNumber, viewModel.bookConfig) { viewModel.billingManager.launchPurchaseFlow(activity) }
            } else {
                chapter?.let { ch ->
                    LazyColumn(
                        state = listState,
                        contentPadding = PaddingValues(top = padding.calculateTopPadding() + 8.dp, bottom = padding.calculateBottomPadding() + 8.dp, start = 16.dp, end = 16.dp),
                        verticalArrangement = Arrangement.spacedBy(12.dp)
                    ) {
                        items(ch.paragraphs, key = { it.id }) { paragraph ->
                            ParagraphCard(
                                paragraph = paragraph,
                                speakingId = speakingId,
                                isEnFirst = isEnFirst,
                                showEn = showEn,
                                showKo = showKo,
                                onSentenceClick = { sentenceId -> viewModel.playFromSentence(sentenceId) }
                            )
                        }
                    }
                } ?: Box(modifier = Modifier.fillMaxSize().padding(padding), contentAlignment = Alignment.Center) { CircularProgressIndicator() }
            }
        }
    }
}

@Composable
private fun ParagraphCard(
    paragraph: BilingualParagraph,
    speakingId: String?,
    isEnFirst: Boolean,
    showEn: Boolean,
    showKo: Boolean,
    onSentenceClick: (String) -> Unit
) {
    if (paragraph.is_header) {
        Column(modifier = Modifier.fillMaxWidth().padding(vertical = 8.dp)) {
            if (showEn) {
                Text(text = paragraph.en, style = MaterialTheme.typography.titleLarge, fontWeight = FontWeight.Bold, textAlign = TextAlign.Center, modifier = Modifier.fillMaxWidth())
            }
            if (showKo) {
                Text(text = paragraph.ko, style = MaterialTheme.typography.titleMedium, fontWeight = FontWeight.Bold, color = MaterialTheme.colorScheme.secondary, textAlign = TextAlign.Center, modifier = Modifier.fillMaxWidth())
            }
            HorizontalDivider(modifier = Modifier.padding(top = 8.dp))
        }
        return
    }

    Card(
        modifier = Modifier.fillMaxWidth(),
        colors = CardDefaults.cardColors(containerColor = MaterialTheme.colorScheme.surface),
        elevation = CardDefaults.cardElevation(1.dp)
    ) {
        Column(modifier = Modifier.padding(16.dp)) {
            if (isEnFirst) {
                if (showEn) SentenceBlock(paragraph.en, Language.EN, paragraph.id, speakingId, MaterialTheme.colorScheme.onSurface, onSentenceClick)
                if (showEn && showKo) Spacer(Modifier.height(8.dp).also { HorizontalDivider(color = MaterialTheme.colorScheme.outlineVariant) }.height(8.dp))
                if (showKo) SentenceBlock(paragraph.ko, Language.KO, paragraph.id, speakingId, MaterialTheme.colorScheme.secondary, onSentenceClick)
            } else {
                if (showKo) SentenceBlock(paragraph.ko, Language.KO, paragraph.id, speakingId, MaterialTheme.colorScheme.secondary, onSentenceClick)
                if (showEn && showKo) Spacer(Modifier.height(8.dp).also { HorizontalDivider(color = MaterialTheme.colorScheme.outlineVariant) }.height(8.dp))
                if (showEn) SentenceBlock(paragraph.en, Language.EN, paragraph.id, speakingId, MaterialTheme.colorScheme.onSurface, onSentenceClick)
            }
        }
    }
}

@Composable
private fun SentenceBlock(
    text: String,
    lang: Language,
    paragraphId: Int,
    speakingId: String?,
    textColor: Color,
    onClick: (String) -> Unit
) {
    val highlightColor = MaterialTheme.colorScheme.primaryContainer
    
    val sentences = remember(text) { SentenceSplitter.split(text, lang, paragraphId) }
    
    val annotatedString = buildAnnotatedString {
        sentences.forEach { s ->
            val isHighlighted = s.id == speakingId
            val start = length
            append(s.text + " ")
            val end = length
            
            addStringAnnotation(tag = "SENTENCE", annotation = s.id, start = start, end = end)
            addStyle(style = SpanStyle(color = textColor, background = if (isHighlighted) highlightColor else Color.Transparent), start = start, end = end)
        }
    }

    ClickableText(
        text = annotatedString,
        style = MaterialTheme.typography.bodyLarge.copy(lineHeight = 26.sp),
        onClick = { offset ->
            annotatedString.getStringAnnotations(tag = "SENTENCE", start = offset, end = offset).firstOrNull()?.let {
                onClick(it.item)
            }
        }
    )
}

@Composable
private fun ReaderBottomBar(
    isSpeaking: Boolean,
    isAccessible: Boolean,
    onPrevious: () -> Unit,
    onNext: () -> Unit,
    onPlayPause: () -> Unit
) {
    BottomAppBar {
        Row(modifier = Modifier.fillMaxWidth(), horizontalArrangement = Arrangement.SpaceEvenly, verticalAlignment = Alignment.CenterVertically) {
            IconButton(onClick = onPrevious) { Icon(Icons.AutoMirrored.Filled.ArrowBack, contentDescription = "Previous Sentence") }
            FloatingActionButton(
                onClick = onPlayPause,
                containerColor = if (isAccessible) MaterialTheme.colorScheme.primary else MaterialTheme.colorScheme.surfaceVariant
            ) {
                Icon(imageVector = if (isSpeaking) Icons.Default.Stop else Icons.Default.PlayArrow, contentDescription = if (isSpeaking) "Stop" else "Play")
            }
            IconButton(onClick = onNext) { Icon(Icons.AutoMirrored.Filled.ArrowForward, contentDescription = "Next Sentence") }
        }
    }
}

@Composable
private fun PaywallScreen(chapterNumber: Int, bookConfig: com.tkprof.shared.model.BookConfig, onBuy: () -> Unit) {
    Box(modifier = Modifier.fillMaxSize().background(MaterialTheme.colorScheme.background), contentAlignment = Alignment.Center) {
        Column(horizontalAlignment = Alignment.CenterHorizontally, verticalArrangement = Arrangement.spacedBy(16.dp), modifier = Modifier.padding(32.dp)) {
            Icon(Icons.Default.Lock, contentDescription = null, modifier = Modifier.size(64.dp), tint = MaterialTheme.colorScheme.primary)
            Text(stringResource(R.string.paywall_locked_desc, chapterNumber), style = MaterialTheme.typography.headlineSmall, fontWeight = FontWeight.Bold, textAlign = TextAlign.Center)
            Text(stringResource(R.string.paywall_purchase_desc), style = MaterialTheme.typography.bodyMedium, textAlign = TextAlign.Center, color = MaterialTheme.colorScheme.onSurfaceVariant)
            Button(onClick = onBuy, modifier = Modifier.fillMaxWidth()) { Icon(Icons.Default.ShoppingCart, contentDescription = null); Spacer(Modifier.width(8.dp)); Text(stringResource(R.string.btn_unlock_now)) }
        }
    }
}






