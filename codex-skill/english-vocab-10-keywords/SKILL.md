---
name: english-vocab-10-keywords
description: Create or revise a reusable 10-keyword English learning video from a reference sample, adapting the topic, words, icons, voice, music, timing, and layout while preserving the sample style.
---

# English Vocab - Listen & Choose

## Approved template profile

- Display name: `Everyday English – Listen & Choose – Green Center Timer (Hybrid Voice)`
- Quick name: `/everyday-english-10-guess-reveal`
- The approved structure is documented in `TEMPLATE_EVERYDAY_ENGLISH_GUESS_REVEAL_HYBRID.md` in the opened video project.
- The approved Mode B implementation is the `video-template` project delivered alongside this skill.

This public starter currently includes a runnable Mode B renderer. Mode A remains a documented creative variant, but its renderer is not included here; do not promise an exportable Mode A video from this starter without adding that implementation.

Use this as the single reusable template for short Vietnamese-English vocabulary videos. The current approved default is the Mode B source-template grammar. For new episodes, change the topic, word pairs, Vietnamese explanations, matched visuals, and voice assets only; preserve the approved composition, timer behavior, reveal rhythm, audio balance, and CTA unless the user explicitly requests a structural change.

For handoff, keep the skill folder separate from the editable video project. The companion setup guide explains installation and service configuration. Never package real API keys or `.env` files; provide only an example config with empty secret fields.

## Core output

- Create one short-form video with 10 practical English words or phrases by default. For Mode B, use five two-choice cards to show 10 choices; the included sample starts with four cards.
- Show or read the Vietnamese meaning first, then reveal and read the English item after a short delay.
- Keep the video vertical at 1080x1920, 30 fps, and under 60 seconds.
- Use one topic-matched visual or 3D-style icon for each item. Do not reuse an unrelated icon set when the topic changes.
- Use ElevenLabs v3 with the approved native English voice for English narration.
- Use the configured, authorized CIT Voice Studio voice for Vietnamese support narration; keep Vietnamese and English as separate audio segments.
- Keep speech clearly above the background music and sound effects.
- For the approved Mode B default, use two choices per card, a green timer bar that contracts symmetrically toward the exact center, a red correct label at reveal, a Vietnamese explanation panel after reveal, and a separate spoken CTA ending.

## Supported reference modes

### Mode A: Guess and reveal

Use this mode when the reference has a moving vertical background, a dark translucent card, a masked word, a short countdown, and a final answer reveal.

- Use 10 words or short phrases in one episode.
- Show the item number, a clue or Vietnamese meaning, and a masked English phrase with only a few letters hidden so the phrase remains recognizable.
- Use a three-second listening window with a progress bar and the text `You have 3 seconds`; do not show a visible `3–2–1` countdown.
- Place the consistent 3D clock/check learning icon below the card.
- Reveal the full English phrase and pronunciation after the pause.
- A 5 to 6 second rhythm per item keeps 10 items below 60 seconds.
- Suitable visuals include a slow vertical background loop plus one consistent timer, check, or answer icon.
- The waiting state must reserve exactly three seconds before reveal. The spoken English phrase must start only at the reveal boundary.
- End with a complete CTA card, keep it visible until the Vietnamese CTA finishes, hold briefly, and fade out the final video and audio.
- Add a topic-matched 3D-style icon or real cutout image for every item when the selected episode calls for item visuals; never reuse unrelated icons.

### Mode B: Listen and choose

Use this mode when the reference has a clean light background, two visual choices, large English labels, and one choice changing color after the audio cue.

- Use 5 cards with 2 options each when the target is 10 visible words. The approved sample has 4 cards/8 visible words because it follows the supplied reference; expand to 5 cards when the episode brief asks for 10 words.
- Play or read one target word, leave a short guessing pause, then highlight the correct option.
- Use minimal pairs or commonly confused words, such as quantity/quality or finally/family.
- Keep each card close to 5 to 6 seconds so the full episode remains below 60 seconds.
- Prefer simple, high-contrast illustrations or isolated object images with matching labels.
- Reserve the fixed listening window defined by the timing sheet, then highlight the answer. Do not add a visible numeric countdown unless the user asks for one.
- Use the light paper background, matched real cutout/3D visual pair, green symmetric center timer, 3D stopwatch, post-reveal Vietnamese explanation, and a spoken CTA card as the default Mode B grammar.

Select one mode per episode unless the user explicitly requests a hybrid. Do not mix two visual grammars halfway through a video.

## Reference-sample workflow

1. Inspect the supplied sample and write a compact style brief covering composition, background, card shape, typography, colors, icon treatment, reveal timing, pauses, transitions, music, and sound effects.
2. Preserve the useful structure of the sample, but adapt the words, examples, visuals, and pacing to the new topic.
3. Choose the 10 most common and immediately useful words or phrases for the audience. Prefer natural workplace or daily-life usage over obscure vocabulary.
4. Prepare a matching icon or image for every row. Verify that each visual semantically matches its word.
5. Build the Vietnamese-first, English-second voice sequence. Leave an intentional intro hold before the first item and a short, consistent pause between items.
6. Render a preview, then check timing, text visibility, icon placement, audio balance, and that item 1 cannot overlap the intro or item 2.

## Default Mode B production recipe

When the user asks to create a new video from this template without requesting a new layout:

1. Build the content table first: pair, correct choice, Vietnamese explanation, pronunciation, and one semantically matched visual per choice.
2. Reuse the source-template renderer and timing/mixer logic in the currently opened video project; do not assume a machine-specific absolute path.
3. Keep the green timer line centered at the start and contract both ends equally until they meet at x=540; never move the line toward the selected side.
4. Show the explanation panel only after the correct label is revealed, below the stopwatch, with enough hold time to read it.
5. End with the approved CTA structure: `NICE WORK!`, a short review summary, `LƯU VIDEO`, `LUYỆN LẠI`, `THEO DÕI KÊNH`, and a soft fade-out. Generate a fresh Vietnamese CTA when the topic/count changes.
6. Keep the hybrid audio order: CIT Vietnamese intro/CTA, ElevenLabs v3 English target words, low music bed, and restrained reveal cue.
7. Validate the final render at 1080×1920, 30 fps, under 60 seconds, with the visual and audio boundaries derived from one timing source.

## Asset search checklist

Collect assets only after the mode and topic are selected.

### Backgrounds

- Mode A: one or two slow vertical 9:16 loops with clear dark areas behind text. Search terms: `vertical waterfall aerial`, `Vietnam nature vertical video`, `Southeast Asia city night vertical`, `Vietnam cafe b roll vertical`, `remote work desk vertical`.
- Mode B: a clean off-white paper or soft texture background, preferably static or with very subtle movement. Search terms: `paper texture off white vertical`, `minimal classroom background`, `clean education background 9:16`.
- Prefer Vietnam or ASEAN locations when the topic benefits from local context. Check commercial-use terms before publishing.

### Icons and images

- Mode A: one timer or progress icon and one small reveal/check icon; keep the set consistent.
- Mode B: two isolated images or 3D-style icons per card, one for each word. Use transparent PNG or clean SVG where possible.
- Do not distribute visuals extracted from a reference video unless the owner has confirmed rights to redistribute them. The public starter intentionally omits those example cutouts.
- Search terms: `3D icon [word] transparent PNG`, `flat illustration [word]`, `[word] object cutout`, `[word] vs [word] visual pair`.
- Build a semantic mapping table so every icon matches the exact word. Never reuse a delivery icon for an office or family word.

### Music and sound effects

- Music: `light educational quiz`, `soft upbeat learning`, `minimal lo-fi background`, `playful vocabulary game`.
- Mode A SFX: soft countdown tick, short whoosh for the reveal, gentle correct chime, low-volume progress pop.
- Mode B SFX: short listening cue, answer-selection click, subtle correct chime, very light transition whoosh.
- Keep the music and SFX clearly below the ElevenLabs v3 narration. Duck the bed during every spoken line.

### Voice

- Use the approved native English ElevenLabs v3 voice for English phrases.
- Use CIT Voice Studio for Vietnamese narration and CTA.
- Generate separate Vietnamese and English segments so timing can be adjusted without changing the visual layout.
- Leave a real listening pause before the reveal or answer highlight; do not place English text on screen before the spoken cue.
- Keep a timing sheet for every item: target audio start, countdown start, countdown seconds, reveal/highlight time, and end of card.

## Included project

The distributable project is `video-template/`. It contains the Mode B paired-choice renderer, timing logic, hybrid voice generator, mixer, `.env.example`, and a Windows setup script. It does not contain the old reference-video cutouts, voice samples, or finished example video.

Useful files:

- `reference_modes_data.py` for the episode's paired vocabulary, Vietnamese explanations, and visual filenames.
- `reference_timing.py` for the shared timing source.
- `generate_reference_mode_b_hybrid_voice.py` for Vietnamese CIT and English ElevenLabs v3 audio.
- `render_reference_mode_b_source_template.py` for the visual render.
- `mix_reference_modes.py` for music, cue, narration, and final video assembly.
- `generate_starter_audio.py` for original local starter music and cue files.
- `source_research/reference_b_cutouts/` for user-provided original or licensed visuals; absent files render as clearly marked placeholders.

The included sample data has four pairs. If adding a fifth pair for 10 visible choices, update the content, images, narration, CTA wording, and check that the complete export remains under 60 seconds.

## Timing and audio defaults

- Start with an intro hold of about 0.8 seconds before the first row unless the reference requires another value.
- Reveal English after Vietnamese with an intentional delay of about 0.72 seconds, then adjust to the reference sample.
- Keep total duration comfortably below 60 seconds.
- Use the selected ElevenLabs v3 English voice and configured CIT Voice Studio Vietnamese voice as separate tracks.
- Lower voice gain enough to avoid clipping and keep the music bed noticeably quieter than speech.
- Add subtle, relevant sound effects only when they improve the rhythm; never let them cover the words.
- Validate timing by checking the intro hold, each three-second guessing window, each reveal boundary, and the full CTA ending. The CTA must not be shorter than its spoken audio.

## Starter content patterns

- Everyday vocabulary: 10 common words with an object or scene icon.
- Work and remote work: 10 phrases used in chat, meetings, deadlines, and delivery of work.
- Service jobs: 10 phrases for nail salons, restaurants, hotels, retail, or food delivery.
- Pronunciation challenge: 5 minimal-pair cards containing 10 visible words.

For every episode, store the Vietnamese meaning, English text, pronunciation, optional example sentence, icon query, and target highlight state together. This prevents the text, audio, and visual from drifting out of sync.

## Important boundaries

- This is one general 10-keyword template, not a collection of topic-specific skills.
- Food delivery, nail salon, hotel front desk, restaurant, retail, remote work, and marketing are example episodes only.
- Do not create a new skill for each topic unless the user explicitly asks for separate templates.
- When the user sends another sample, analyze that sample first and then update the episode data and rendering choices.
