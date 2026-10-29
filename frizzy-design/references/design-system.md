# Design system, motion, and style

Contents
- How the design layer works
- Step 1: find the direction (reference or default)
- Step 2: skills to lean on
- Step 3: tokens
- Typography
- Icons
- Motion stack and rules
- Style flavors
- Per-surface guidance
- Accessibility floor
- Changing the design later
- What the PRD's design section contains

## How the design layer works

The design is a separate layer that the rest of the PRD does not depend on. Behavior, flows, data, and API stay the same when the look changes. To make that true, the PRD describes the design as tokens (named values for color, type, space, shape, shadow, and motion), a component list that consumes those tokens, and a direction statement that explains the intent. Swapping a reference means editing the direction and the token values, then adjusting the components that used special cases. Nothing else moves.

Say this in the PRD in one or two sentences so the owner knows the look can change without redoing the plan.

## Step 1: find the direction

Case A: the person sent a reference (screenshots, links, a moodboard, or words such as "Awwwards-style, dark, kinetic type").

1. Look at every image. Describe what you see in plain terms: layout structure, density, grid, palette, contrast, type families and weights, corner radius, borders versus shadows, imagery style, iconography, and the feel of motion if a video or description gives hints.
2. If an image file is available in a shell, sample dominant colors with a small script (Pillow's `quantize` or a k-means pass) to get real hex values instead of guessing. State that values are sampled approximations.
3. Name fonts only when you can identify them with confidence. Otherwise name the closest open-licensed alternatives and say they are stand-ins.
4. Write a reference mapping table: what was taken from each reference, what was left out, and what was adapted for the product's context. Do not copy a brand's distinctive assets, logos, or exact layouts. Describe qualities and rebuild them.
5. Write a one-line design read: "Reading this as: <surface> for <audience>, with a <vibe> language, leaning toward <system or style flavor>."

Case B: no reference. Infer a direction from the audience, product category, and the vibe words in the brief, then state it. Use the three dials from the taste skill as a shared vocabulary (each from 1 to 10): variance (symmetry to experimental), motion intensity (static to cinematic), and visual density (airy to packed). Reasonable starting points: calm productivity tools around 4/3/4, consumer products 7/6/3, creative and agency sites 9/8/3, public-sector and trust-first products 3/2/5. Marketing and portfolio surfaces can run higher on variance and motion than the product UI behind them.

Never ask for a reference as a blocker. Offer it once (the intake rules in project-frizzy) and move on.

## Step 2: skills to lean on

These skills improve the build stage. Check which ones are installed (frizzy-test's environment check lists them). If one is missing, give the install command and ask before installing; do not install on your own.

Emil Kowalski's skills (install: `npx skills@latest add emilkowalski/skills`), from the repository's own list:
- `emil-design-eng`: the main skill, mostly animation craft with some design advice.
- `animate`: builds an animation from scratch with a chosen curve, duration, and properties.
- `review-animations` and `improve-animations`: strict review and prioritized fixes.
- `find-animation-opportunities`: where motion helps and where it should be left out.
- `animation-performance`: fixes dropped frames.
- `animation-vocabulary`: words for describing motion precisely.
- `apple-design`: Apple interface principles translated for the web.
- `pick-ui-library`: picks maintained libraries instead of hand-rolling or choosing abandoned ones.
- `mobile-native`: makes a web app feel native on a phone.
- `break-ui`: tries to break the UI with worst-case data.
- `prototype`: builds several variants of a piece of UI behind a switcher.

Taste skill by Leonxlnx (install: `npx skills add https://github.com/Leonxlnx/taste-skill --skill "design-taste-frontend"`). It targets landing pages, portfolios, and redesigns, not dashboards or data-heavy product UI. Variants in the collection include minimalist, brutalist, high-end visual design, redesign-existing-projects, and image-led design skills. Use it for marketing and brand surfaces, and use Emil's skills plus a component library for product screens.

Recommended split: taste skill for the look of marketing and brand surfaces, Emil's skills for interaction and motion quality everywhere, a real component library (shadcn/ui, Radix, or the platform's own) for product UI.

When the skills are not installed, the PRD still states the principles in your own words. Typical principles from this body of work, confirm against the installed skill when available:
- Entering elements use ease-out curves; ease-in feels sluggish on entrances.
- Interface feedback finishes quickly (well under 300 ms for most UI), and larger transitions earn longer durations.
- Elements do not grow from scale 0; start near 0.95 with opacity.
- Popovers and menus scale from their trigger (transform-origin set to the anchor).
- Pressable controls give a small press response (a slight scale-down).
- Animate transform and opacity; avoid animating layout properties.
- Respect `prefers-reduced-motion` by removing movement and keeping fades.
- Semi-transparent shadows usually look better than solid borders on layered surfaces.

## Step 3: tokens

Define tokens as CSS custom properties (and the Tailwind v4 `@theme` block if Tailwind is used), with light and dark values. Write the actual values in the PRD, not placeholders, so a developer can paste them.

| Token group | Contents |
|---|---|
| Color roles | Background, surface, surface-raised, border, text, text-muted, accent, accent-text, success, warning, danger, focus ring. Each role has light and dark values. |
| Contrast check | Every text and interactive pair meets WCAG 2.2 AA (4.5:1 body text, 3:1 large text and UI components). Record the ratios. |
| Type scale | Font families, sizes (fluid with clamp), line heights, weights, tracking |
| Space | A scale based on a 4 or 8 px unit |
| Shape | Radii (none, small, medium, large, full), border widths |
| Elevation | Shadow levels, blur and layered shadows |
| Motion | Durations (instant, fast, base, slow), easings (standard, enter, exit, spring), stagger step, distance values |
| Layout | Breakpoints, container widths, grid columns and gutters, safe-area handling |
| Z-index | Named layers (base, sticky, overlay, modal, toast) |

Calculate every contrast ratio with `scripts/contrast.py` and write the real numbers into the table. Do not estimate them. Include a short code block with the starting tokens and note that components must reference tokens, never raw values. The same token file feeds web, and its values can be exported for native or game UI.

## Typography

Choose a pairing with a reason tied to the direction (editorial serif plus neutral sans; geometric display plus mono for technical products; a pixel or bitmap face for retro games). Rules for the PRD:

- Prefer open-licensed fonts (SIL OFL) from Fontsource or the foundry's own download, self-hosted with `font-display: swap`, subsetted to needed glyphs, with a real fallback stack. Avoid third-party font CDNs in privacy-sensitive regions.
- One or two families, a limited weight set, and a variable font when it saves bytes.
- Measure and rhythm: 45 to 75 characters per line for reading text, line height 1.4 to 1.7 for body, tighter for display sizes.
- Kinetic or animated type (split text, scramble, variable-weight hover, marquee) is allowed in hero and brand moments. Keep body text static, keep it readable to screen readers (real text in the DOM, not images), and respect reduced motion.
- Document licenses in an appendix, since fonts are a common source of legal surprise.

## Icons

Choose one icon family for the whole project and one stroke weight. Candidates, all with open licenses or generous terms: Phosphor, Hugeicons, Tabler, Radix Icons, and Lucide (the taste skill discourages Lucide by default; use it when the project already depends on it or the owner asks). Do not hand-draw icon paths; if a glyph is missing, add a second library only after checking the style matches, or compose from primitives.

Animated icons are welcome as micro-interactions: CSS or Motion transitions on SVG paths, Lottie for pre-made sequences, Rive for interactive state machines. Keep each icon animation under about 600 ms, make it triggered by hover, focus, or state change (not looping), and provide a static fallback.

Specify in the PRD: library, size scale (16, 20, 24), stroke width, color rules (inherit text color), and the mapping of key actions to icons.

## Motion stack and rules

Pick the lightest tool that does the job. State the choice and the reason in a motion table.

| Need | Tool | Notes |
|---|---|---|
| Hover, focus, small state changes | CSS transitions and `@starting-style` | Zero JavaScript. Default choice. |
| Route and view transitions | View Transitions API with a fallback | Progressive enhancement; check browser support at build time |
| Component enter, exit, layout, gestures in React | Motion (`motion/react`) | Good for springs and layout animation. Use motion values for continuous input instead of React state. |
| Timelines, scroll-driven sequences, text splitting, SVG morphing, Flip | GSAP with ScrollTrigger, SplitText, Flip, MorphSVG | GSAP is free for commercial use under the Webflow-era standard license, including formerly paid plugins. Read the license for edge cases such as tools that let end users build animations visually. |
| Smooth scrolling | Lenis | Pair with GSAP ScrollTrigger when both are used. Keep native behavior for anchor links, keyboard scrolling, and reduced motion. Consider disabling it on touch devices. |
| Ready-made animated components and backgrounds | React Bits | Copy-in components (text effects, backgrounds, cursors). License is MIT with the Commons Clause: fine inside your product, not allowed to sell the components themselves. Check bundle cost per component. |
| Particles | tsParticles or a small canvas script | Cap particle count by device; pause when off screen |
| 3D and shaders | Three.js with react-three-fiber, OGL, or raw WebGL | Lazy-load; provide a static poster fallback; budget GPU time |
| Pre-made vector animation | Lottie (dotLottie) | Check file size; prefer Rive when interactivity matters |
| Interactive state-driven animation | Rive | Runtime is free; design files need the Rive editor |
| Physics | Matter.js or Rapier | Use only when physics is the feature |

Rules to write into the PRD:

1. A motion map table: each interaction (hover, press, focus, page enter, scroll reveal, modal, toast, loading, success, error, empty state) with its pattern, tool, duration, and easing.
2. A performance budget: animate transform and opacity, stay at 60 fps on a mid-range phone, lazy-load heavy effects, pause off-screen work, keep animation JavaScript under a stated size, and watch Interaction to Next Paint and Cumulative Layout Shift.
3. A reduced-motion plan: with `prefers-reduced-motion: reduce`, replace movement with fades or nothing, stop autoplay loops, and keep all information available.
4. A mobile plan: lighter effects on touch devices, no scroll hijacking, no hover-only features.
5. Restraint: motion should explain what changed, give feedback, or set mood in a hero moment. Remove motion that only fills time. Use the find-animation-opportunities mindset to say what is deliberately not animated.
6. Signature moments: pick one to three hero moments per surface (an opening sequence, a scroll story, a satisfying success state). Product UI stays quieter than marketing UI.

## Style flavors

A flavor is a distinctive visual language layered on the base system. The default is one base system plus at most one flavor and one accent flavor. A flavor can lead on marketing, brand, and game surfaces and stay light on dense product screens. For each flavor the PRD records: where it applies, the token changes, the assets it needs, and the fallback when motion or effects are turned off.

| Flavor | Look | How to build it | Watch for |
|---|---|---|---|
| Particles | Drifting or interactive dots, constellations, dust | tsParticles, canvas, or a React Bits background | CPU use on phones; pause off-screen; low-contrast text over particles |
| Liquid morph | Blobs and shapes that flow into each other | SVG filters (gooey effect), GSAP MorphSVG, or shader gradients | Filter cost; provide static shapes under reduced motion |
| Neon glow | Dark surfaces, saturated edges, bloom | Layered `box-shadow` and `text-shadow`, mix-blend modes, subtle flicker | Contrast and eye strain; avoid glow on body text |
| Y2K chrome | Metallic gradients, bubbles, stars, glossy buttons | Multi-stop gradients, inner shadows, SVG or 3D chrome objects, rounded display type | Overuse; keep content areas plain |
| Kinetic type | Words that move, stretch, or react to scroll and cursor | GSAP SplitText, variable fonts, CSS scroll-driven animation | Real text in the DOM; reduced motion; reading comfort |
| Paper cutout | Layered torn paper, drop shadows, collage | SVG clip-paths, rough edges, layered shadows, slight rotations | Shadow consistency; image weight |
| Holographic | Iridescent gradients that shift with angle | Conic and linear gradients, `background-blend-mode`, pointer-driven angle | Contrast; gradient banding; keep text on solid chips |
| Isometric | 30-degree blocks, tiled scenes, diagrams | CSS transforms, SVG, or Three.js with an orthographic camera | Hit areas on transformed elements; accessibility of diagrams |
| ASCII art | Monospace characters as imagery and textures | Text art in `pre`, canvas ASCII shader, mono fonts | Screen readers (use `aria-hidden` and a real label); line height alignment |
| Clay 3D | Soft inflated shapes, pastel, rounded lighting | Pre-rendered images, or Three.js with soft materials, or layered CSS shadows | Image weight; keep the 3D optional on slow devices |
| Retro VHS | Scanlines, chromatic aberration, tracking glitches | CSS gradients and filters, SVG displacement, canvas noise | Seizure risk from flicker; reduce intensity and motion on request |
| Comic book | Halftone dots, bold outlines, speech bubbles | CSS radial-gradient halftones, thick borders, skewed panels, display fonts | Text legibility in bubbles; localization |
| Split flap | Airport-board flipping characters | CSS 3D flips or GSAP timelines per character | Announce the final text to screen readers; duration for long strings |
| Hand drawn | Sketchy lines, wobble, marker fills | rough.js, SVG filters (turbulence), hand-lettered fonts | Consistency across components; cost of many filtered elements |
| Blueprint | Cyan grids, white line art, technical annotations | CSS grid backgrounds, SVG line drawing (stroke-dashoffset), mono labels | Line contrast; density on mobile |
| Physics | Draggable, falling, colliding elements | Matter.js, Rapier, or Motion's drag and spring | Keyboard alternatives for every drag; mobile performance |
| Pixel art | Crisp pixels, limited palettes, bitmap fonts | `image-rendering: pixelated`, integer scaling, canvas, sprite sheets | Blurry scaling; text size for legibility |
| Bauhaus | Primary colors, geometric shapes, strict grid | CSS grid, solid shapes, bold sans type | Avoid gimmicky shape clutter; keep a clear hierarchy |
| Art Deco | Symmetry, gold lines, fans and sunbursts, elegant display type | SVG ornaments, thin borders, high-contrast serif or geometric type | Ornament weight; dark-mode contrast of metallic tones |
| Neo-brutalism | Thick black borders, hard offset shadows, flat bright color | Solid borders, `box-shadow` with zero blur, chunky type | Dense forms feel heavy; keep spacing generous |
| Glass and aurora | Frosted panels over soft gradients | `backdrop-filter`, layered borders, mesh or radial gradients | Provide solid fallbacks for reduced transparency; label as approximation, not Apple's material |
| Bento and editorial | Tiled grids, large type, asymmetric layout | CSS Grid with mixed spans, serif display type | Reading order on mobile |

Combining rules:
- One base system plus one lead flavor is the default. A second flavor appears only in a contained area (hero, empty state, 404 page).
- Flavors must work in the token system: colors, radii, shadows, and type come from tokens so a swap is a token change plus a few components.
- Every flavor needs a calm mode: a reduced-motion and reduced-effects version that keeps the identity through color, shape, and type.

## Per-surface guidance

- Marketing and brand pages: variance and motion can run high. Keep a clear primary action above the fold, real content and imagery, and a speed budget (LCP under about 2.5 seconds on a mid-range phone).
- Product UI and dashboards: density and clarity lead. Use a component library, restrained motion, keyboard support, and strong empty, loading, and error states. Apply break-ui thinking: long names, huge counts, empty lists.
- Mobile apps: follow platform conventions (Apple Human Interface Guidelines, Material 3) unless the brand deliberately departs. Touch targets of 44 points or more, safe areas, thumb reach, haptics where available, gesture alternatives.
- Browser extensions: design for the popup size limit and for the host page's styles (isolate with Shadow DOM when injecting UI).
- Pixel-art games: fix one internal resolution and scale by whole numbers only, define a small named palette as tokens and compute contrast for every text pair, bundle fonts inside the game so no font CDN is called, give every effect a calm-mode version, and keep icons as sprites inside the same palette.
- Games: HUD readability at distance, controller and keyboard navigation, scalable UI, color-blind-safe palettes, subtitles with size options, and an art direction document (shape language, palette, reference boards, animation principles, audio tone).
- Email and documents: keep to web-safe fonts and simple layout. Do not carry web motion into email.

## Accessibility floor

- WCAG 2.2 level AA as the target. Contrast ratios as above, visible focus indicators, full keyboard use, labels for every control, error messages that explain the fix, and target sizes of at least 24 CSS pixels (44 recommended on touch).
- Motion: no flashing above three times per second, pause controls for autoplay, reduced-motion support.
- Do not rely on color alone, provide captions and transcripts for media, test with a screen reader on at least one platform, and add axe checks to CI.

## Changing the design later

When the person sends a new reference or asks for a different look:

1. Read the new input with the Case A procedure above.
2. Update the direction statement, reference mapping table, flavor choice, and token values in the PRD's design section. Keep token names stable so components do not change.
3. List components that need edits beyond tokens (special shapes, custom backgrounds, new motion).
4. Update the motion map, icon choice, and typography if they changed, and adjust the screen descriptions that mention the old look.
5. Leave user flows, features, data, API, and costs alone, except for asset or library costs the new style adds.
6. Re-run the linter. During the build, compare screenshots at 375, 768, 1280, and 1920 pixel widths with playwright-cli against the reference.
7. Add a line to the PRD changelog.

## What the PRD's design section contains

1. Design read and direction statement (two or three sentences).
2. Reference mapping table (when references exist) and how to supply or change them.
3. Base system and style flavor, with reasons and fallbacks.
4. Tokens with real values, light and dark, plus contrast ratios.
5. Typography, with licenses.
6. Icon library and rules.
7. Motion map, motion stack, performance budget, and reduced-motion plan.
8. Component inventory with states (default, hover, focus, active, disabled, loading, error, empty).
9. Layout and responsive rules, and ASCII wireframes for the key screens.
10. Imagery, illustration, and audio guidelines with licensing notes.
11. Accessibility targets.
12. The swap protocol in two or three lines.
