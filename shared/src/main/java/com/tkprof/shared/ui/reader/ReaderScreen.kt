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
import androidx.compose.foundation.gestures.awaitEachGesture
import androidx.compose.foundation.gestures.awaitFirstDown
import androidx.compose.ui.input.pointer.pointerInput
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
import androidx.compose.ui.text.style.TextOverflow
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
import androidx.lifecycle.Lifecycle
import androidx.lifecycle.LifecycleEventObserver
import androidx.lifecycle.compose.LocalLifecycleOwner

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun ReaderScreen(viewModel: ReaderViewModel) {
    val chapter by viewModel.currentChapter.collectAsState()
    val chapterNumber by viewModel.currentChapterNumber.collectAsState()
    val totalChapters by viewModel.totalChapters.collectAsState()
    val chapterTitles by viewModel.chapterTitles.collectAsState()
    val speakingId by viewModel.speakingSentenceId.collectAsState()
    val isPlaying by viewModel.isPlaying.collectAsState()
    val isFullUnlocked by viewModel.isFullUnlocked.collectAsState()
    val bypassedUpToChapter by viewModel.bypassedUpToChapter.collectAsState()
    val maxAccessible = maxOf(viewModel.bookConfig.freeChapters, bypassedUpToChapter + 2)
    val showSoftPaywall = !isFullUnlocked && chapterNumber > maxAccessible
    val isAccessible = !showSoftPaywall
    val languageOrder by viewModel.languageOrder.collectAsState()
    val showEn by viewModel.showEn.collectAsState()
    val showKo by viewModel.showKo.collectAsState()
    val activity = LocalContext.current as Activity

    val speakingParagraphIndex by viewModel.speakingParagraphIndex.collectAsState()

    var showSettings by remember { mutableStateOf(false) }
    var resumeTrigger by remember { mutableStateOf(0) }
    
    val lifecycleOwner = LocalLifecycleOwner.current
    DisposableEffect(lifecycleOwner) {
        val observer = LifecycleEventObserver { _, event ->
            if (event == Lifecycle.Event.ON_RESUME) resumeTrigger++
        }
        lifecycleOwner.lifecycle.addObserver(observer)
        onDispose { lifecycleOwner.lifecycle.removeObserver(observer) }
    }
    
    val drawerState = rememberDrawerState(initialValue = DrawerValue.Closed)
    val scope = rememberCoroutineScope()
    val drawerListState = rememberLazyListState()

    LaunchedEffect(drawerState.isOpen) {
        if (drawerState.isOpen && totalChapters > 0) {
            val targetIndex = (chapterNumber - 1).coerceIn(0, totalChapters - 1)
            val scrollOffsetIndex = maxOf(0, targetIndex - 2)
            drawerListState.scrollToItem(scrollOffsetIndex)
        }
    }

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
                    LazyColumn(
                        state = drawerListState,
                        modifier = Modifier.weight(1f)
                    ) {
                        items(totalChapters) { index ->
                            val i = index + 1
                            val accessible = viewModel.isChapterAccessible(i)
                            
                            val titleObj = chapterTitles.getOrNull(index)
                            val displayTitle = if (titleObj != null) {
                                val firstLang = languageOrder.firstOrNull { it == Language.EN || it == Language.KO }
                                if (firstLang == Language.KO) titleObj.ko else titleObj.en
                            } else {
                                stringResource(R.string.chapter_label, i)
                            }

                            NavigationDrawerItem(
                                label = {
                                    Text(
                                        text = displayTitle,
                                        style = MaterialTheme.typography.bodyMedium.copy(
                                            fontFamily = androidx.compose.ui.text.font.FontFamily.Serif,
                                            fontSize = 14.sp,
                                            lineHeight = 19.sp,
                                            fontWeight = if (i == chapterNumber) FontWeight.SemiBold else FontWeight.Normal
                                        ),
                                        maxLines = 1,
                                        overflow = TextOverflow.Ellipsis,
                                        color = if (accessible) LocalContentColor.current else MaterialTheme.colorScheme.onSurface.copy(alpha = 0.38f)
                                    )
                                },
                                badge = {
                                    if (!accessible) {
                                        Icon(Icons.Default.Lock, contentDescription = null, modifier = Modifier.size(16.dp), tint = MaterialTheme.colorScheme.onSurface.copy(alpha = 0.38f))
                                    }
                                },
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
                                    activity.startActivity(Intent(Intent.ACTION_VIEW, Uri.parse("market://search?q=pub:Billy+Wookyoung+Hong")))
                                } catch(e: ActivityNotFoundException) {
                                    activity.startActivity(Intent(Intent.ACTION_VIEW, Uri.parse("https://play.google.com/store/apps/developer?id=Billy+Wookyoung+Hong")))
                                }
                            },
                            modifier = Modifier.fillMaxWidth()
                        ) {
                            Text(stringResource(R.string.more_books_btn))
                        }
                        
                        Spacer(modifier = Modifier.height(16.dp))
                        Button(
                            onClick = {
                                viewModel.billingManager.launchPurchaseFlow(activity, "tip_small_1500")
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
    ) {
        Scaffold(
            topBar = {
                TopAppBar(
                    title = {
                        Column {
                            Text(
                                text = viewModel.bookConfig.titleEn, 
                                style = MaterialTheme.typography.titleMedium,
                                maxLines = 1,
                                overflow = TextOverflow.Ellipsis
                            )
                            val titleObj = chapterTitles.getOrNull(chapterNumber - 1)
                            val displayTitle = if (titleObj != null) {
                                val firstLang = languageOrder.firstOrNull { it == Language.EN || it == Language.KO }
                                if (firstLang == Language.KO) titleObj.ko else titleObj.en
                            } else {
                                "Chapter $chapterNumber"
                            }
                            Text(
                                text = "$displayTitle ($chapterNumber / $totalChapters)", 
                                style = MaterialTheme.typography.bodySmall, 
                                color = MaterialTheme.colorScheme.onSurfaceVariant,
                                maxLines = 1,
                                overflow = TextOverflow.Ellipsis
                            )
                        }
                    },
                    navigationIcon = {
                        IconButton(
                            onClick = { scope.launch { drawerState.open() } }
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
                    isSpeaking = isPlaying,
                    isAccessible = isAccessible,
                    onPrevious = { viewModel.previousSentence() },
                    onNext = { viewModel.nextSentence() },
                    onPlayPause = { viewModel.playOrPause() }
                )
            }
        ) { padding ->
                    val listState = rememberLazyListState()
                    val fontSizeMultiplier by viewModel.fontSizeMultiplier.collectAsState()

                    // Scroll to top whenever the chapter changes
                    LaunchedEffect(chapterNumber) {
                        listState.scrollToItem(0)
                    }

                    // Scroll to active paragraph when it changes or app resumes
                    LaunchedEffect(speakingParagraphIndex, resumeTrigger) {
                        if (speakingParagraphIndex >= 0) {
                            val visibleItems = listState.layoutInfo.visibleItemsInfo
                            val isVisible = visibleItems.any { it.index == speakingParagraphIndex }
                            if (!isVisible || resumeTrigger > 0) {
                                listState.animateScrollToItem(speakingParagraphIndex)
                            }
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
                                    languageOrder = languageOrder,
                                    showEn = showEn,
                                    showKo = showKo,
                                    fontSizeMultiplier = fontSizeMultiplier,
                                    onSentenceClick = { sentenceId -> viewModel.playFromSentence(sentenceId) }
                                )
                            }
                        }
                        
                        // Custom Interactive Scrollbar
                        val isScrollbarVisible = listState.layoutInfo.totalItemsCount > 0
                        if (isScrollbarVisible) {
                            val totalItems = listState.layoutInfo.totalItemsCount
                            val visibleItems = listState.layoutInfo.visibleItemsInfo.size
                            val firstVisible = listState.firstVisibleItemIndex
                            
                            var isDragging by remember { mutableStateOf(false) }

                            if (visibleItems < totalItems) {
                                BoxWithConstraints(
                                    modifier = Modifier
                                        .align(Alignment.TopEnd)
                                        .fillMaxHeight()
                                        .width(32.dp) // Wide invisible touch area
                                        .padding(vertical = 8.dp)
                                        .pointerInput(totalItems) {
                                            awaitEachGesture {
                                                val down = awaitFirstDown()
                                                isDragging = true
                                                val trackHeightPx = size.height.toFloat()
                                                
                                                fun updateScroll(y: Float) {
                                                    val proportion = (y / trackHeightPx).coerceIn(0f, 1f)
                                                    val targetItem = (proportion * totalItems).toInt().coerceIn(0, totalItems - 1)
                                                    scope.launch { listState.scrollToItem(targetItem) }
                                                }
                                                
                                                updateScroll(down.position.y)
                                                
                                                do {
                                                    val event = awaitPointerEvent()
                                                    val change = event.changes.firstOrNull()
                                                    if (change != null && change.pressed) {
                                                        change.consume()
                                                        updateScroll(change.position.y)
                                                    }
                                                } while (event.changes.any { it.pressed })
                                                isDragging = false
                                            }
                                        }
                                ) {
                                    val trackHeight = maxHeight
                                    val scrollProportion = firstVisible.toFloat() / (totalItems - visibleItems)
                                    val thumbHeightFraction = (visibleItems.toFloat() / totalItems).coerceIn(0.05f, 1f)
                                    
                                    Box(
                                        modifier = Modifier
                                            .align(Alignment.CenterEnd)
                                            .fillMaxHeight()
                                            .width(if (isDragging) 12.dp else 8.dp)
                                            .padding(end = 4.dp)
                                            .background(MaterialTheme.colorScheme.onSurface.copy(alpha = 0.2f), shape = androidx.compose.foundation.shape.RoundedCornerShape(4.dp))
                                    ) {
                                        Box(
                                            modifier = Modifier
                                                .fillMaxWidth()
                                                .fillMaxHeight(thumbHeightFraction)
                                                .offset(y = (trackHeight - (trackHeight * thumbHeightFraction)) * scrollProportion)
                                                .background(
                                                    if (isDragging) MaterialTheme.colorScheme.primary else MaterialTheme.colorScheme.primary.copy(alpha = 0.8f),
                                                    shape = androidx.compose.foundation.shape.RoundedCornerShape(4.dp)
                                                )
                                        )
                                    }
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
    languageOrder: List<Language>,
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
            languageOrder.forEach { lang ->
                when (lang) {
                    Language.EN -> if (showEn && paragraph.en.isNotBlank()) SentenceBlock(paragraph.en, Language.EN, paragraph.id, speakingId, MaterialTheme.colorScheme.onSurface, enTextStyle, onSentenceClick)
                    Language.KO -> if (showKo && paragraph.ko.isNotBlank()) SentenceBlock(paragraph.ko, Language.KO, paragraph.id, speakingId, MaterialTheme.colorScheme.secondary, koTextStyle, onSentenceClick)
                    else -> {}
                }
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
            val visibleBlocks = mutableListOf<@Composable () -> Unit>()
            for (lang in languageOrder) {
                when (lang) {
                    Language.EN -> if (showEn && paragraph.en.isNotBlank()) visibleBlocks.add { SentenceBlock(paragraph.en, Language.EN, paragraph.id, speakingId, MaterialTheme.colorScheme.onSurface, enTextStyle, onSentenceClick) }
                    Language.KO -> if (showKo && paragraph.ko.isNotBlank()) visibleBlocks.add { SentenceBlock(paragraph.ko, Language.KO, paragraph.id, speakingId, MaterialTheme.colorScheme.secondary, koTextStyle, onSentenceClick) }
                    else -> {}
                }
            }
            visibleBlocks.forEachIndexed { index, block ->
                block()
                if (index < visibleBlocks.size - 1) {
                    Spacer(Modifier.height(8.dp).also { HorizontalDivider(color = MaterialTheme.colorScheme.outlineVariant) }.height(8.dp))
                }
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
            // Pad the bounding box by 350dp above and below.
            // This forces the scrolling list to place the sentence near the center of the screen,
            // rather than stopping the moment it barely crosses the bottom edge.
            val padding = with(density) { 350.dp.toPx() }
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
            TextButton(onClick = onNotNow, modifier = Modifier.fillMaxWidth()) { Text(stringResource(R.string.btn_not_now)) }
        }
    }
}






