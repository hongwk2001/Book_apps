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
import androidx.compose.foundation.relocation.BringIntoViewRequester
import androidx.compose.foundation.relocation.bringIntoViewRequester
import androidx.compose.ui.platform.LocalDensity
import androidx.compose.ui.unit.IntOffset
import androidx.compose.ui.geometry.Rect
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
    val bypassedUpToChapter by viewModel.bypassedUpToChapter.collectAsState()
    val showSoftPaywall = !isFullUnlocked && (chapterNumber % 3 == 0) && (bypassedUpToChapter < chapterNumber)
    val isAccessible = !showSoftPaywall
    val isEnFirst by viewModel.isEnFirst.collectAsState()
    val showEn by viewModel.showEn.collectAsState()
    val showKo by viewModel.showKo.collectAsState()
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
        gesturesEnabled = !showSoftPaywall,
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
                        
                        if (!isFullUnlocked) {
                            Spacer(modifier = Modifier.height(16.dp))
                            Button(
                                onClick = {
                                    // Use first tip id or open a tip dialog. We can just open the Soft Paywall Screen or a tip dialog.
                                    // For simplicity, launch purchase flow for small tip, or we can just scroll to paywall.
                                    // But wait, the plan says "Add a persistent 'Support Developer' button so users can tip at any time without waiting for the paywall".
                                    // Let's just launch the small tip flow for now or all of them.
                                    viewModel.billingManager.launchPurchaseFlow(activity, "tip_medium_3000")
                                },
                                modifier = Modifier.fillMaxWidth(),
                                colors = ButtonDefaults.buttonColors(containerColor = MaterialTheme.colorScheme.tertiary)
                            ) {
                                Text(stringResource(R.string.btn_support_developer))
                            }
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
                        IconButton(
                            onClick = { if (!showSoftPaywall) scope.launch { drawerState.open() } },
                            enabled = !showSoftPaywall
                        ) {
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
                    val fontSizeMultiplier by viewModel.fontSizeMultiplier.collectAsState()
                    
                    LaunchedEffect(speakingParagraphIndex, chapter) {
                        if (speakingParagraphIndex >= 0) {
                            kotlinx.coroutines.delay(150)
                            listState.animateScrollToItem(speakingParagraphIndex)
                        }
                    }

                    if (showSoftPaywall) {
                SoftPaywallScreen(
                    onTip = { tipId -> viewModel.billingManager.launchPurchaseFlow(activity, tipId) },
                    onNotNow = { viewModel.bypassSoftPaywall() }
                )
            } else {
                chapter?.let { ch ->
                    // Wrapping in a Box to draw the scrollbar
                    Box(modifier = Modifier.fillMaxSize().padding(padding)) {
                        LazyColumn(
                            state = listState,
                            contentPadding = PaddingValues(top = 8.dp, bottom = 8.dp, start = 16.dp, end = 16.dp),
                            verticalArrangement = Arrangement.spacedBy(12.dp)
                        ) {
                            items(ch.paragraphs, key = { it.id }) { paragraph ->
                                ParagraphCard(
                                    paragraph = paragraph,
                                    speakingId = speakingId,
                                    isEnFirst = isEnFirst,
                                    showEn = showEn,
                                    showKo = showKo,
                                    fontSizeMultiplier = fontSizeMultiplier,
                                    onSentenceClick = { sentenceId -> viewModel.playFromSentence(sentenceId) }
                                )
                            }
                        }
                        
                        // Custom Scrollbar
                        val isScrollbarVisible = listState.layoutInfo.totalItemsCount > 0
                        if (isScrollbarVisible) {
                            val totalItems = listState.layoutInfo.totalItemsCount
                            val visibleItems = listState.layoutInfo.visibleItemsInfo.size
                            val firstVisible = listState.firstVisibleItemIndex
                            
                            if (visibleItems < totalItems) {
                                BoxWithConstraints(
                                    modifier = Modifier
                                        .align(Alignment.TopEnd)
                                        .fillMaxHeight()
                                        .padding(end = 4.dp, top = 8.dp, bottom = 8.dp)
                                        .width(4.dp)
                                        .background(MaterialTheme.colorScheme.onSurface.copy(alpha = 0.1f))
                                ) {
                                    val scrollProportion = firstVisible.toFloat() / (totalItems - visibleItems)
                                    val thumbHeightFraction = (visibleItems.toFloat() / totalItems).coerceIn(0.1f, 1f)
                                    val trackHeight = maxHeight
                                    
                                    Box(
                                        modifier = Modifier
                                            .fillMaxWidth()
                                            .fillMaxHeight(thumbHeightFraction)
                                            .offset(y = (trackHeight - (trackHeight * thumbHeightFraction)) * scrollProportion)
                                            .background(MaterialTheme.colorScheme.primary, shape = androidx.compose.foundation.shape.RoundedCornerShape(2.dp))
                                    )
                                }
                            }
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
    fontSizeMultiplier: Float,
    onSentenceClick: (String) -> Unit
) {
    val enTextStyle = if (paragraph.is_header) {
        MaterialTheme.typography.titleLarge.copy(fontWeight = FontWeight.Bold, textAlign = TextAlign.Center, lineHeight = (30 * fontSizeMultiplier).sp, fontSize = (22 * fontSizeMultiplier).sp)
    } else {
        MaterialTheme.typography.bodyLarge.copy(lineHeight = (26 * fontSizeMultiplier).sp, fontSize = (16 * fontSizeMultiplier).sp)
    }

    val koTextStyle = if (paragraph.is_header) {
        MaterialTheme.typography.titleMedium.copy(fontWeight = FontWeight.Bold, textAlign = TextAlign.Center, lineHeight = (26 * fontSizeMultiplier).sp, fontSize = (18 * fontSizeMultiplier).sp)
    } else {
        MaterialTheme.typography.bodyLarge.copy(lineHeight = (26 * fontSizeMultiplier).sp, fontSize = (16 * fontSizeMultiplier).sp)
    }

    if (paragraph.is_header) {
        Column(modifier = Modifier.fillMaxWidth().padding(vertical = 8.dp)) {
            if (showEn) SentenceBlock(paragraph.en, Language.EN, paragraph.id, speakingId, MaterialTheme.colorScheme.onSurface, enTextStyle, onSentenceClick)
            if (showKo) SentenceBlock(paragraph.ko, Language.KO, paragraph.id, speakingId, MaterialTheme.colorScheme.secondary, koTextStyle, onSentenceClick)
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
                if (showEn) SentenceBlock(paragraph.en, Language.EN, paragraph.id, speakingId, MaterialTheme.colorScheme.onSurface, enTextStyle, onSentenceClick)
                if (showEn && showKo) Spacer(Modifier.height(8.dp).also { HorizontalDivider(color = MaterialTheme.colorScheme.outlineVariant) }.height(8.dp))
                if (showKo) SentenceBlock(paragraph.ko, Language.KO, paragraph.id, speakingId, MaterialTheme.colorScheme.secondary, koTextStyle, onSentenceClick)
            } else {
                if (showKo) SentenceBlock(paragraph.ko, Language.KO, paragraph.id, speakingId, MaterialTheme.colorScheme.secondary, koTextStyle, onSentenceClick)
                if (showEn && showKo) Spacer(Modifier.height(8.dp).also { HorizontalDivider(color = MaterialTheme.colorScheme.outlineVariant) }.height(8.dp))
                if (showEn) SentenceBlock(paragraph.en, Language.EN, paragraph.id, speakingId, MaterialTheme.colorScheme.onSurface, enTextStyle, onSentenceClick)
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
    textStyle: androidx.compose.ui.text.TextStyle,
    onClick: (String) -> Unit
) {
    val highlightColor = MaterialTheme.colorScheme.primaryContainer
    
    val sentences = remember(text) { SentenceSplitter.split(text, lang, paragraphId) }
    
    val requester = remember { BringIntoViewRequester() }
    var highlightY by remember { mutableFloatStateOf(0f) }
    
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

    Box(modifier = Modifier.fillMaxWidth()) {
        ClickableText(
            text = annotatedString,
            style = textStyle,
            modifier = Modifier.fillMaxWidth(),
            onTextLayout = { layoutResult ->
                val annotation = annotatedString.getStringAnnotations("SENTENCE", 0, annotatedString.length)
                    .firstOrNull { it.item == speakingId }
                if (annotation != null) {
                    val rect = layoutResult.getBoundingBox(annotation.start)
                    highlightY = rect.top
                }
            },
            onClick = { offset ->
                annotatedString.getStringAnnotations(tag = "SENTENCE", start = offset, end = offset).firstOrNull()?.let {
                    onClick(it.item)
                }
            }
        )
        
        Spacer(
            modifier = Modifier
                .padding(top = with(LocalDensity.current) { highlightY.toDp() })
                .size(1.dp)
                .bringIntoViewRequester(requester)
        )
    }
    
    val density = LocalDensity.current
    LaunchedEffect(speakingId, highlightY) {
        if (sentences.any { it.id == speakingId }) {
            // Pad the bounding box by 250dp above and below.
            // This forces the scrolling list to place the sentence near the center of the screen,
            // rather than stopping the moment it barely crosses the bottom edge.
            val padding = with(density) { 250.dp.toPx() }
            requester.bringIntoView(Rect(0f, -padding, 1f, padding))
        }
    }
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
            IconButton(onClick = onPrevious, enabled = isAccessible) { Icon(Icons.AutoMirrored.Filled.ArrowBack, contentDescription = "Previous Sentence") }
            FloatingActionButton(
                onClick = { if (isAccessible) onPlayPause() },
                containerColor = if (isAccessible) MaterialTheme.colorScheme.primary else MaterialTheme.colorScheme.surfaceVariant,
                contentColor = if (isAccessible) MaterialTheme.colorScheme.onPrimary else MaterialTheme.colorScheme.onSurfaceVariant.copy(alpha = 0.38f)
            ) {
                Icon(imageVector = if (isSpeaking) Icons.Default.Stop else Icons.Default.PlayArrow, contentDescription = if (isSpeaking) "Stop" else "Play")
            }
            IconButton(onClick = onNext, enabled = isAccessible) { Icon(Icons.AutoMirrored.Filled.ArrowForward, contentDescription = "Next Sentence") }
        }
    }
}

@Composable
private fun SoftPaywallScreen(onTip: (String) -> Unit, onNotNow: () -> Unit) {
    Box(modifier = Modifier.fillMaxSize().background(MaterialTheme.colorScheme.background).verticalScroll(rememberScrollState()), contentAlignment = Alignment.Center) {
        Column(horizontalAlignment = Alignment.CenterHorizontally, verticalArrangement = Arrangement.spacedBy(16.dp), modifier = Modifier.padding(32.dp)) {
            Icon(Icons.Default.Favorite, contentDescription = null, modifier = Modifier.size(64.dp), tint = MaterialTheme.colorScheme.primary)
            Text(stringResource(R.string.tip_jar_message), style = MaterialTheme.typography.bodyLarge, textAlign = TextAlign.Center)
            Spacer(Modifier.height(16.dp))
            Button(onClick = { onTip("tip_small_1500") }, modifier = Modifier.fillMaxWidth()) { Text(stringResource(R.string.tip_small)) }
            Button(onClick = { onTip("tip_medium_3000") }, modifier = Modifier.fillMaxWidth()) { Text(stringResource(R.string.tip_medium)) }
            Button(onClick = { onTip("tip_large_5000") }, modifier = Modifier.fillMaxWidth()) { Text(stringResource(R.string.tip_large)) }
            TextButton(onClick = onNotNow, modifier = Modifier.fillMaxWidth()) { Text(stringResource(R.string.btn_not_now)) }
        }
    }
}






