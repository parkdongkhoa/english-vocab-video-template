# Everyday English – Listen & Choose – Green Center Timer (Hybrid Voice)

Quick name: `/everyday-english-10-guess-reveal`

Approved default: **Mode B source-template**. For future episodes, replace the content and matched visuals while keeping this visual/audio grammar unless the user explicitly asks for a different structure.

## Purpose

Reusable vertical English-learning video template for 10 common words or phrases. Replace the episode topic, vocabulary, Vietnamese clues, pronunciation, background, and topic-matched icons while preserving the approved visual and timing grammar.

## Locked format

- Canvas: 1080×1920, 30 fps, under 60 seconds.
- Layout: blurred real/contextual vertical background; `EVERYDAY ENGLISH` header pill; centered dark translucent card; 3D clock/check icon below the card.
- Intro: short hold before item 1 so the first Vietnamese line never collides with the title card.
- Each item: `WORD X OF 10 • GUESS THE PHRASE` → masked English phrase with only a few letters hidden → Vietnamese clue → three-second progress bar → full English phrase and IPA pronunciation.
- The screen does not display a visible `3–2–1`; the waiting period is communicated by the progress bar and `You have 3 seconds`.
- Each phrase must remain visible long enough for the viewer to recognize the complete phrase, not just one isolated word.
- End card: `NICE WORK!` / `10 phrases reviewed` / `Save this video and review it twice`.
- CTA audio must finish completely, followed by a short hold and a gentle fade-out.

## Approved Mode B default

- Use the clean light paper background and the two-choice layout from the supplied reference.
- Keep the green timer bar centered as a full-width line at the start; contract both ends equally until they meet at the exact center. Do not slide the bar toward the selected option.
- Keep the 3D stopwatch beneath the timer. After reveal, change only the correct label to red and show a Vietnamese explanation panel below the stopwatch.
- Finish with a dedicated CTA card: `NICE WORK!`, a short review summary, `LƯU VIDEO`, `LUYỆN LẠI`, `THEO DÕI KÊNH`, and a soft fade-out.
- Preserve the hybrid audio order: CIT Vietnamese intro/CTA, ElevenLabs v3 English target word, low music bed, and restrained reveal cue.

## Voice and audio

- Vietnamese support voice: CIT Voice Studio. The project owner's preferred voice is `Đoan Trang`; each recipient configures a voice available and authorized in their own CIT service.
- English learning voice: ElevenLabs v3, approved English voice `Matilda`.
- Read Vietnamese first; reveal and read English only after the guessing window.
- Keep narration clearly above the music bed and sound effects.
- Music stays low; use a soft countdown tick during the three-second window and a light reveal cue at the answer boundary.

## Mode B variant — Listen & Choose

- Keep the clean light background and two-choice card grammar from the second reference.
- Use four source-matched minimal-pair cards in the bundled sample, with one original or licensed visual per option. Preserve transparency where possible, add only a soft ground shadow, and keep objects readable at phone size. The public starter does not include cutouts extracted from the reference video.
- Read the target word in ElevenLabs v3 English, leave the exact choice window, show the 3D stopwatch below the underline, then highlight the correct option.
- Use CIT Voice Studio for the Vietnamese intro and CTA; do not reuse the old all-`Adam` audio set.
- Keep a slightly longer start offset and a short gap after the target word so the first sound is not rushed.
- Finish with a complete CTA audio line, a short hold, and a gentle fade-out.

## Timing rules

1. Keep the intro hold explicit.
2. Start the three-second guessing window only after the Vietnamese clue finishes.
3. Start the English phrase exactly at the reveal boundary.
4. Derive the CTA duration from the actual Vietnamese CTA audio, then add a short visual hold.
5. Verify the final duration is under 60 seconds and that no item overlaps the next item or the CTA.

## Content rules

- Choose 10 high-frequency phrases for the selected audience and situation.
- Match every icon or image to its exact phrase/topic.
- Keep Vietnamese explanations short and natural.
- Keep pronunciation text readable and centered.
- When the topic changes, replace the icon/image set instead of reusing unrelated delivery, office, or service icons.

## Current distributable implementation

- Runnable visual renderer: `render_reference_mode_b_source_template.py`
- Shared Mode B timing source: `reference_timing.py`
- Hybrid voice generator: `generate_reference_mode_b_hybrid_voice.py`
- Audio mixer: `mix_reference_modes.py`
- Starter music and cue generator: `generate_starter_audio.py`
- The public package does not bundle generated voices or a finished sample video. Create fresh media using the recipient's own service access.

## Source-template lock for Mode B

- Use the light paper background and the compact red top label established by the approved reference.
- Keep the large red Vietnamese question with white outline and black shadow.
- Do not add the dark/white option cards, `EVERYDAY ENGLISH` subtitle stack, or visible `3–2–1` numbers from the earlier prototype.
- Place the two topic-matched original/licensed visuals directly on the page, place the English labels beneath them, add the 3D stopwatch below the underline, and animate one green timer bar that contracts symmetrically toward the exact center.
- Change only the correct English label to red at the reveal boundary, then move to the next pair.
- After the reveal, show a compact Vietnamese explanation box below the stopwatch so the meaning of both choices is clear.
- Keep the approved 4-pair episode around 29 seconds; when expanding to 5 pairs/10 visible words, keep the output under 60 seconds and derive the CTA timing from its actual audio duration.
