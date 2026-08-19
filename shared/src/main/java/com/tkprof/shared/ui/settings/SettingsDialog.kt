package com.tkprof.shared.ui.settings

import android.speech.tts.Voice
import android.widget.Toast
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.verticalScroll
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.dp
import androidx.compose.ui.res.stringResource
import com.tkprof.shared.R
import com.tkprof.shared.ui.reader.ReaderViewModel

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun SettingsDialog(
    viewModel: ReaderViewModel,
    onDismiss: () -> Unit
) {
    val context = LocalContext.current
    val ttsManager = viewModel.ttsManager

    val englishVoices by ttsManager.englishVoices.collectAsState()
    val koreanVoices by ttsManager.koreanVoices.collectAsState()

    var isEnFirst by remember { mutableStateOf(viewModel.isEnFirst.value) }
    var showEn by remember { mutableStateOf(viewModel.showEn.value) }
    var showKo by remember { mutableStateOf(viewModel.showKo.value) }
    var readEn by remember { mutableStateOf(viewModel.readEn.value) }
    var readKo by remember { mutableStateOf(viewModel.readKo.value) }

    var selectedEnVoice by remember { mutableStateOf(ttsManager.selectedEnglishVoice) }
    var selectedKoVoice by remember { mutableStateOf(ttsManager.selectedKoreanVoice) }
    var enSpeed by remember { mutableFloatStateOf(ttsManager.englishSpeed) }
    var koSpeed by remember { mutableFloatStateOf(ttsManager.koreanSpeed) }
    var enPitch by remember { mutableFloatStateOf(ttsManager.englishPitch) }
    var koPitch by remember { mutableFloatStateOf(ttsManager.koreanPitch) }

    fun ensureShowConstraint(newShowEn: Boolean, newShowKo: Boolean) {
        if (!newShowEn && !newShowKo) {
            Toast.makeText(context, context.getString(R.string.toast_one_lang_visible), Toast.LENGTH_SHORT).show()
            showEn = true
            showKo = true
        } else {
            showEn = newShowEn
            showKo = newShowKo
            if (!showEn) readEn = false
            if (!showKo) readKo = false
        }
    }

    AlertDialog(
        onDismissRequest = onDismiss,
        title = { Text(stringResource(R.string.settings_title)) },
        text = {
            Column(
                modifier = Modifier
                    .verticalScroll(rememberScrollState())
                    .padding(vertical = 8.dp),
                verticalArrangement = Arrangement.spacedBy(16.dp)
            ) {
                // Top Level: Language Order
                Text(stringResource(R.string.language_order_title), style = MaterialTheme.typography.labelLarge)
                Row(modifier = Modifier.fillMaxWidth(), horizontalArrangement = Arrangement.SpaceBetween, verticalAlignment = Alignment.CenterVertically) {
                    Text(stringResource(if (isEnFirst) R.string.order_en_ko else R.string.order_ko_en))
                    Switch(checked = isEnFirst, onCheckedChange = { isEnFirst = it })
                }

                HorizontalDivider()

                // Checkboxes following Language Order
                Text(stringResource(R.string.display_tts_title), style = MaterialTheme.typography.labelLarge)
                
                @Composable
                fun LangControls(lang: String, isEn: Boolean) {
                    Row(modifier = Modifier.fillMaxWidth(), verticalAlignment = Alignment.CenterVertically) {
                        Text(lang, modifier = Modifier.weight(1f))
                        Column(horizontalAlignment = Alignment.CenterHorizontally) {
                            Text(stringResource(R.string.setting_show), style = MaterialTheme.typography.labelSmall)
                            Checkbox(
                                checked = if (isEn) showEn else showKo,
                                onCheckedChange = { if (isEn) ensureShowConstraint(it, showKo) else ensureShowConstraint(showEn, it) }
                            )
                        }
                        Spacer(modifier = Modifier.width(16.dp))
                        Column(horizontalAlignment = Alignment.CenterHorizontally) {
                            Text(stringResource(R.string.setting_read), style = MaterialTheme.typography.labelSmall)
                            Checkbox(
                                checked = if (isEn) readEn else readKo,
                                onCheckedChange = { if (isEn) readEn = it else readKo = it },
                                enabled = if (isEn) showEn else showKo
                            )
                        }
                    }
                }

                if (isEnFirst) {
                    LangControls(stringResource(R.string.lang_english), true)
                    LangControls(stringResource(R.string.lang_korean), false)
                } else {
                    LangControls(stringResource(R.string.lang_korean), false)
                    LangControls(stringResource(R.string.lang_english), true)
                }

                HorizontalDivider()

                // English Voice Controls
                Text(stringResource(R.string.english_voice_title), style = MaterialTheme.typography.labelLarge)
                VoiceDropdown(
                    voices = englishVoices,
                    selected = selectedEnVoice,
                    onSelect = {
                        selectedEnVoice = it
                        ttsManager.selectedEnglishVoice = it
                        ttsManager.speakSample(true, viewModel.bookConfig.titleEn)
                    }
                )
                Text(stringResource(R.string.setting_speed, enSpeed), style = MaterialTheme.typography.bodySmall)
                Slider(value = enSpeed, onValueChange = { enSpeed = it }, valueRange = 0.5f..3.0f)
                
                Text(stringResource(R.string.setting_pitch, enPitch), style = MaterialTheme.typography.bodySmall)
                Slider(value = enPitch, onValueChange = { enPitch = it }, valueRange = 0.5f..2.0f)

                HorizontalDivider()

                // Korean Voice Controls
                Text(stringResource(R.string.korean_voice_title), style = MaterialTheme.typography.labelLarge)
                VoiceDropdown(
                    voices = koreanVoices,
                    selected = selectedKoVoice,
                    onSelect = {
                        selectedKoVoice = it
                        ttsManager.selectedKoreanVoice = it
                        ttsManager.speakSample(false, viewModel.bookConfig.titleKo)
                    }
                )
                Text(stringResource(R.string.setting_speed, koSpeed), style = MaterialTheme.typography.bodySmall)
                Slider(value = koSpeed, onValueChange = { koSpeed = it }, valueRange = 0.5f..3.0f)
                
                Text(stringResource(R.string.setting_pitch, koPitch), style = MaterialTheme.typography.bodySmall)
                Slider(value = koPitch, onValueChange = { koPitch = it }, valueRange = 0.5f..2.0f)
            }
        },
        confirmButton = {
            TextButton(onClick = {
                // Apply everything
                viewModel.showEn.value = showEn
                viewModel.showKo.value = showKo
                viewModel.readEn.value = readEn
                viewModel.readKo.value = readKo
                if (viewModel.isEnFirst.value != isEnFirst) {
                    viewModel.updateLanguageOrder(isEnFirst)
                }
                
                ttsManager.selectedEnglishVoice = selectedEnVoice
                ttsManager.selectedKoreanVoice = selectedKoVoice
                ttsManager.englishSpeed = enSpeed
                ttsManager.koreanSpeed = koSpeed
                ttsManager.englishPitch = enPitch
                ttsManager.koreanPitch = koPitch
                
                onDismiss()
            }) { Text(stringResource(R.string.btn_apply)) }
        },
        dismissButton = {
            TextButton(onClick = onDismiss) { Text(stringResource(R.string.btn_cancel)) }
        }
    )
}

@OptIn(ExperimentalMaterial3Api::class)
@Composable
private fun VoiceDropdown(
    voices: List<Voice>,
    selected: Voice?,
    onSelect: (Voice) -> Unit
) {
    var expanded by remember { mutableStateOf(false) }
    ExposedDropdownMenuBox(
        expanded = expanded,
        onExpandedChange = { expanded = it }
    ) {
        OutlinedTextField(
            value = selected?.name ?: "Default",
            onValueChange = {},
            readOnly = true,
            label = { Text("Voice") },
            trailingIcon = { ExposedDropdownMenuDefaults.TrailingIcon(expanded) },
            modifier = Modifier.menuAnchor(ExposedDropdownMenuAnchorType.PrimaryNotEditable, true).fillMaxWidth()
        )
        ExposedDropdownMenu(
            expanded = expanded,
            onDismissRequest = { expanded = false }
        ) {
            voices.forEach { voice ->
                DropdownMenuItem(
                    text = { Text(voice.name) },
                    onClick = {
                        onSelect(voice)
                        expanded = false
                    }
                )
            }
        }
    }
}

