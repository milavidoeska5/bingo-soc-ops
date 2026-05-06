# Bingo Soc Ops — Design Specification
## Playful, Vibrant CSS Palette & Animation System

**Version**: 1.0  
**Last Updated**: May 6, 2026  
**Status**: Design Phase

---

## 1. Color Palette

### Primary Colors
| Name | Hex | Purpose | Notes |
|------|-----|---------|-------|
| **Vibrant Purple** | `#7C3AED` | Primary action, headers, emphasis | Bold, energetic; main brand color |
| **Soft Lavender** | `#E9D5FF` | Light backgrounds, soft accents | Pastel counterpart to vibrant purple |
| **Bright Teal** | `#14B8A6` | Secondary action, highlights | Playful, fresh, complementary |
| **Soft Mint** | `#D1FAE5` | Light backgrounds, subtle fills | Gentle pastel teal |

### Accent Colors
| Name | Hex | Purpose | Notes |
|------|-----|---------|-------|
| **Hot Pink** | `#EC4899` | CTA buttons, celebration, marked squares | Eye-catching, celebratory |
| **Soft Pink** | `#FBCFE8` | Light backgrounds, hover states | Pastel pink |
| **Sunny Yellow** | `#FBBF24` | Warnings, highlights, FREE SPACE | Warm, attention-grabbing |
| **Soft Yellow** | `#FEF3C7` | Light accents, backgrounds | Gentle, warm pastel |
| **Vibrant Orange** | `#F97316` | Secondary accents, success states | Energetic, warm |
| **Soft Orange** | `#FFEDD5` | Light fills, subtle backgrounds | Pastel orange |

### Text Colors
| Name | Hex | Purpose | Notes |
|------|-----|---------|-------|
| **Dark Text** | `#1F2937` | Body text, primary readable text | High contrast on light backgrounds |
| **Medium Text** | `#4B5563` | Secondary text, labels | Slightly lighter, for hierarchy |
| **Light Text** | `#F3F4F6` | Text on dark/vibrant backgrounds | Off-white for readability |
| **White** | `#FFFFFF` | Text on dark overlays, buttons | Pure white for maximum contrast |

### Background Colors
| Name | Hex | Purpose | Notes |
|------|-----|---------|-------|
| **Page Background** | `#FAFAFA` | Main page background | Very light gray, almost white |
| **Card Background** | `#FFFFFF` | Cards, modals, containers | Pure white for clarity |
| **Overlay Dark** | `rgba(31, 41, 55, 0.85)` | Modal overlays | Dark with transparency |
| **Overlay Light** | `rgba(255, 255, 255, 0.95)` | Light overlay for depth | Nearly opaque white |

### Gradient Combinations
| Name | CSS | Purpose | Notes |
|------|-----|---------|-------|
| **Purple-to-Pink** | `linear-gradient(135deg, #7C3AED 0%, #EC4899 100%)` | Hero sections, CTA buttons | Bold, energetic |
| **Teal-to-Mint** | `linear-gradient(135deg, #14B8A6 0%, #D1FAE5 100%)` | Game board background | Playful, fresh |
| **Pastel Rainbow** | `linear-gradient(90deg, #E9D5FF 0%, #D1FAE5 25%, #FEF3C7 50%, #FFEDD5 75%, #FBCFE8 100%)` | Celebratory sections | Playful, light |
| **Glow Effect** | `radial-gradient(circle, rgba(236, 72, 153, 0.4) 0%, transparent 70%)` | Marked square glow | Pink radial glow |

---

## 2. Typography

### Font Stack
```css
/* System fonts, playful CSS enhancements */
font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif;
```

### Heading Styles

#### h1 — Main Title / Hero
```css
font-size: 3.5rem;           /* 56px */
font-weight: 900;            /* Black */
letter-spacing: 0.05em;      /* 2.8px at 56px */
text-transform: none;
line-height: 1.1;
text-shadow: 0 4px 12px rgba(124, 58, 237, 0.15);  /* Subtle purple shadow */
color: #1F2937;              /* Dark text */
transform: scaleY(1.05);     /* Slight vertical stretch for impact */
```

#### h2 — Section Headers / Subtitles
```css
font-size: 2rem;             /* 32px */
font-weight: 800;            /* Extra bold */
letter-spacing: 0.02em;      /* 0.64px */
line-height: 1.25;
text-shadow: 0 2px 8px rgba(124, 58, 237, 0.1);
color: #7C3AED;              /* Vibrant purple */
```

#### h3 — Card Titles / Labels
```css
font-size: 1.25rem;          /* 20px */
font-weight: 700;            /* Bold */
letter-spacing: 0.01em;      /* 0.2px */
line-height: 1.4;
color: #1F2937;
```

### Body Text
```css
font-size: 1rem;             /* 16px */
font-weight: 400;            /* Regular */
line-height: 1.6;
letter-spacing: 0;
color: #4B5563;              /* Medium text */
```

### Button Text
```css
font-size: 1.125rem;         /* 18px */
font-weight: 700;            /* Bold */
letter-spacing: 0.025em;     /* 0.45px */
text-transform: uppercase;
color: #FFFFFF;              /* White for contrast */
```

### Small Text / Metadata
```css
font-size: 0.875rem;         /* 14px */
font-weight: 500;            /* Medium */
letter-spacing: 0.02em;      /* 0.28px */
color: #9CA3AF;              /* Light gray */
```

---

## 3. Animation System

### Timing Functions & Durations
- **Quick interactions**: 150–200ms (hover, focus, simple state changes)
- **Smooth transitions**: 250–350ms (modal enters, complex state changes)
- **Celebratory**: 600–1000ms (BINGO animations, marked square celebrations)

### Keyframe Definitions

#### Pulse Glow (Marked Squares)
```css
@keyframes pulse-glow {
  0%, 100% {
    box-shadow: 0 0 0 0 rgba(236, 72, 153, 0.7),
                inset 0 0 0 0 rgba(236, 72, 153, 0.2);
  }
  50% {
    box-shadow: 0 0 0 12px rgba(236, 72, 153, 0),
                inset 0 0 0 3px rgba(236, 72, 153, 0.1);
  }
}

animation: pulse-glow 2s ease-in-out infinite;
```

#### Bingo Glow (Winning Line)
```css
@keyframes bingo-glow {
  0%, 100% {
    text-shadow: 0 0 10px rgba(236, 72, 153, 0.8),
                 0 0 20px rgba(124, 58, 237, 0.6);
    transform: scale(1);
  }
  50% {
    text-shadow: 0 0 20px rgba(236, 72, 153, 1),
                 0 0 40px rgba(124, 58, 237, 0.8),
                 0 0 60px rgba(251, 191, 36, 0.6);
    transform: scale(1.05);
  }
}

animation: bingo-glow 1.2s ease-in-out infinite;
```

#### Scale Pop (Button Press / Mark)
```css
@keyframes scale-pop {
  0% {
    transform: scale(1);
  }
  50% {
    transform: scale(1.08);
  }
  100% {
    transform: scale(1);
  }
}

animation: scale-pop 0.4s cubic-bezier(0.68, -0.55, 0.265, 1.55);
```

#### Bounce In (Modal Entry)
```css
@keyframes bounce-in {
  0% {
    opacity: 0;
    transform: scale(0.85) translateY(20px);
  }
  60% {
    opacity: 1;
    transform: scale(1.05) translateY(-5px);
  }
  80% {
    transform: scale(0.95) translateY(2px);
  }
  100% {
    opacity: 1;
    transform: scale(1) translateY(0);
  }
}

animation: bounce-in 0.5s cubic-bezier(0.34, 1.56, 0.64, 1);
```

#### Gentle Float (Continuous, Subtle)
```css
@keyframes gentle-float {
  0%, 100% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(-8px);
  }
}

animation: gentle-float 3s ease-in-out infinite;
```

#### Shimmer (Loading / Attention)
```css
@keyframes shimmer {
  0% {
    background-position: -1000px 0;
  }
  100% {
    background-position: 1000px 0;
  }
}

animation: shimmer 2s infinite;
```

#### Rainbow Pulse (Celebratory, rare)
```css
@keyframes rainbow-pulse {
  0%, 100% {
    color: #7C3AED;
  }
  25% {
    color: #EC4899;
  }
  50% {
    color: #14B8A6;
  }
  75% {
    color: #F97316;
  }
}

animation: rainbow-pulse 1.5s ease-in-out;
```

---

## 4. Utility Class Naming

### Color Classes
```css
/* Backgrounds */
.bg-primary-soft { background-color: #E9D5FF; }
.bg-primary-vibrant { background-color: #7C3AED; }
.bg-secondary-soft { background-color: #D1FAE5; }
.bg-secondary-vibrant { background-color: #14B8A6; }
.bg-accent-hot-pink { background-color: #EC4899; }
.bg-accent-sunny { background-color: #FBBF24; }
.bg-accent-orange { background-color: #F97316; }
.bg-page { background-color: #FAFAFA; }
.bg-card { background-color: #FFFFFF; }

/* Text Colors */
.text-primary { color: #1F2937; }
.text-secondary { color: #4B5563; }
.text-light { color: #F3F4F6; }
.text-white { color: #FFFFFF; }
.text-accent-pink { color: #EC4899; }
.text-accent-yellow { color: #FBBF24; }
.text-accent-purple { color: #7C3AED; }
.text-accent-teal { color: #14B8A6; }
```

### Typography Classes
```css
/* Heading Styles */
.text-bold-title { 
  font-weight: 900; 
  letter-spacing: 0.05em; 
  text-shadow: 0 4px 12px rgba(124, 58, 237, 0.15);
}
.text-bold-header { 
  font-weight: 800; 
  letter-spacing: 0.02em; 
  text-shadow: 0 2px 8px rgba(124, 58, 237, 0.1);
}
.text-bold-label { 
  font-weight: 700; 
  letter-spacing: 0.01em; 
}

/* Button Text */
.text-button { 
  font-weight: 700; 
  letter-spacing: 0.025em; 
  text-transform: uppercase; 
}

/* Body Text (Clean) */
.text-readable { 
  font-weight: 400; 
  line-height: 1.6; 
  letter-spacing: 0; 
}

/* Small / Meta */
.text-small-meta { 
  font-size: 0.875rem; 
  font-weight: 500; 
  letter-spacing: 0.02em; 
  color: #9CA3AF; 
}
```

### Shadow & Depth Classes
```css
/* Shadows for different elevations */
.shadow-soft { box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05); }
.shadow-base { box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); }
.shadow-md { box-shadow: 0 10px 15px rgba(0, 0, 0, 0.1); }
.shadow-lg { box-shadow: 0 20px 25px rgba(0, 0, 0, 0.1); }

/* Glow effects */
.glow-pink { box-shadow: 0 0 20px rgba(236, 72, 153, 0.5); }
.glow-purple { box-shadow: 0 0 20px rgba(124, 58, 237, 0.4); }
.glow-teal { box-shadow: 0 0 20px rgba(20, 184, 166, 0.4); }
.glow-intense { box-shadow: 0 0 30px rgba(236, 72, 153, 0.7); }
```

### Animation Classes
```css
/* State animations */
.animate-pulse-glow { animation: pulse-glow 2s ease-in-out infinite; }
.animate-bingo-glow { animation: bingo-glow 1.2s ease-in-out infinite; }
.animate-scale-pop { animation: scale-pop 0.4s cubic-bezier(0.68, -0.55, 0.265, 1.55); }
.animate-bounce-in { animation: bounce-in 0.5s cubic-bezier(0.34, 1.56, 0.64, 1); }
.animate-gentle-float { animation: gentle-float 3s ease-in-out infinite; }
.animate-shimmer { animation: shimmer 2s infinite; }
.animate-rainbow-pulse { animation: rainbow-pulse 1.5s ease-in-out; }

/* Transition classes */
.transition-fast { transition: all 150ms ease-out; }
.transition-base { transition: all 200ms ease-out; }
.transition-smooth { transition: all 300ms cubic-bezier(0.4, 0, 0.2, 1); }
```

### Interactive Classes
```css
/* Hover & Focus States */
.hover-scale { transition: transform 200ms ease-out; }
.hover-scale:hover { transform: scale(1.04); }
.hover-scale:focus { transform: scale(1.02); }

.hover-bright { transition: filter 200ms ease-out; }
.hover-bright:hover { filter: brightness(1.1); }

.hover-shadow { transition: box-shadow 200ms ease-out; }
.hover-shadow:hover { box-shadow: 0 20px 25px rgba(0, 0, 0, 0.15); }

.focus-ring { 
  outline: 2px solid transparent;
  outline-offset: 2px;
}
.focus-ring:focus { 
  outline-color: #7C3AED;
}
```

### Border & Shape Classes
```css
.rounded-soft { border-radius: 0.5rem; }     /* 8px */
.rounded-base { border-radius: 0.75rem; }    /* 12px */
.rounded-lg { border-radius: 1rem; }         /* 16px */
.rounded-full { border-radius: 9999px; }     /* Pill shape */

.border-soft { border: 1px solid #E5E7EB; }
.border-accent { border: 2px solid #7C3AED; }
.border-highlight { border: 2px solid #EC4899; }
```

---

## 5. Component Examples

### Hero CTA Button
```html
<button class="
  bg-purple-to-pink
  text-white
  text-button
  px-8 py-4
  rounded-lg
  shadow-md
  hover-scale
  transition-smooth
  font-weight-700
">
  Play Bingo
</button>
```

**CSS:**
```css
.btn-hero {
  background: linear-gradient(135deg, #7C3AED 0%, #EC4899 100%);
  color: #FFFFFF;
  font-size: 1.125rem;
  font-weight: 700;
  letter-spacing: 0.025em;
  padding: 1rem 2rem;
  border-radius: 1rem;
  border: none;
  box-shadow: 0 10px 25px rgba(236, 72, 153, 0.3);
  transition: all 200ms cubic-bezier(0.4, 0, 0.2, 1);
  cursor: pointer;
}

.btn-hero:hover {
  transform: scale(1.04);
  box-shadow: 0 15px 35px rgba(236, 72, 153, 0.4);
}

.btn-hero:active {
  animation: scale-pop 0.4s cubic-bezier(0.68, -0.55, 0.265, 1.55);
}
```

### Game Board Background
```html
<div class="
  bg-teal-to-mint
  rounded-lg
  shadow-lg
  p-6
">
  <!-- 5x5 bingo grid -->
</div>
```

**CSS:**
```css
.bingo-board {
  background: linear-gradient(135deg, #14B8A6 0%, #D1FAE5 100%);
  border-radius: 1rem;
  padding: 1.5rem;
  box-shadow: 0 20px 25px rgba(0, 0, 0, 0.1);
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 0.5rem;
}
```

### Bingo Square (Unmarked)
```html
<div class="bingo-square" data-index="4">
  <span>Find someone with a pet</span>
</div>
```

**CSS:**
```css
.bingo-square {
  background-color: #FFFFFF;
  border: 2px solid #E5E7EB;
  border-radius: 0.75rem;
  padding: 1rem;
  text-align: center;
  font-size: 0.875rem;
  font-weight: 600;
  color: #1F2937;
  cursor: pointer;
  transition: all 200ms ease-out;
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 80px;
}

.bingo-square:hover {
  transform: scale(1.05);
  border-color: #7C3AED;
  box-shadow: 0 8px 16px rgba(124, 58, 237, 0.2);
}

.bingo-square:focus {
  outline: 2px solid #7C3AED;
  outline-offset: 2px;
}
```

### Bingo Square (Marked)
```html
<div class="bingo-square bingo-square--marked" data-index="4">
  <span>✓</span>
</div>
```

**CSS:**
```css
.bingo-square--marked {
  background: linear-gradient(135deg, #EC4899 0%, #F97316 100%);
  border-color: #EC4899;
  color: #FFFFFF;
  font-size: 1.5rem;
  font-weight: bold;
  box-shadow: 0 0 0 0 rgba(236, 72, 153, 0.7),
              inset 0 0 0 0 rgba(236, 72, 153, 0.2);
  animation: pulse-glow 2s ease-in-out infinite;
}

.bingo-square--marked:hover {
  animation: none;
  transform: scale(1.08);
}
```

### FREE SPACE Center
```html
<div class="bingo-square bingo-square--free" data-index="12">
  <span>FREE</span>
  <span class="text-small">SPACE</span>
</div>
```

**CSS:**
```css
.bingo-square--free {
  background: linear-gradient(135deg, #FBBF24 0%, #FEF3C7 50%, #F97316 100%);
  border: 3px solid #FBBF24;
  color: #1F2937;
  font-weight: 900;
  box-shadow: 0 0 20px rgba(251, 191, 36, 0.4),
              inset 0 0 20px rgba(255, 255, 255, 0.3);
  position: relative;
}

.bingo-square--free::after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: radial-gradient(circle at center, rgba(255, 255, 255, 0.4) 0%, transparent 70%);
  border-radius: 0.75rem;
  animation: gentle-float 3s ease-in-out infinite;
}
```

### Bingo Modal (Celebration)
```html
<div class="modal-overlay">
  <div class="modal modal--celebration">
    <h1 class="text-bold-title animate-bingo-glow">BINGO!</h1>
    <p class="text-secondary">You matched 5 in a row!</p>
    <button class="btn-hero">Play Again</button>
  </div>
</div>
```

**CSS:**
```css
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(31, 41, 55, 0.85);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  backdrop-filter: blur(4px);
  animation: fadeIn 200ms ease-out;
}

.modal {
  background-color: #FFFFFF;
  border-radius: 1rem;
  padding: 3rem;
  max-width: 500px;
  width: 90%;
  box-shadow: 0 25px 50px rgba(0, 0, 0, 0.15);
  animation: bounce-in 0.5s cubic-bezier(0.34, 1.56, 0.64, 1);
}

.modal--celebration {
  background: linear-gradient(135deg, #FEF3C7 0%, #FBCFE8 50%, #E9D5FF 100%);
  border: 3px solid #FBBF24;
}

.modal--celebration h1 {
  color: #7C3AED;
  margin-bottom: 1rem;
  animation: bingo-glow 1.2s ease-in-out infinite;
}
```

### Winning Line Highlight
```html
<div class="bingo-square bingo-square--winning" data-index="0">
  ✓
</div>
```

**CSS:**
```css
.bingo-square--winning {
  background: linear-gradient(135deg, #EC4899 0%, #7C3AED 100%);
  border: 3px solid #7C3AED;
  color: #FFFFFF;
  box-shadow: 0 0 30px rgba(236, 72, 153, 0.7),
              0 0 60px rgba(124, 58, 237, 0.5);
  animation: pulse-glow 1.5s ease-in-out infinite;
}
```

---

## 6. Design Rationale

### Color Choices
- **Purple + Pink gradient**: Vibrant, playful energy; modern and inclusive
- **Teal + Mint**: Fresh, complementary secondary palette; nature-inspired calmness
- **Yellow**: Warm, celebratory, draws attention for FREE SPACE and wins
- **Soft pastels as backgrounds**: Light, accessible, non-fatiguing on eyes
- **High-contrast text**: Readability on all backgrounds (WCAG AA+)

### Animation Philosophy
- **Smooth, not jarring**: All transitions use cubic-bezier for natural motion
- **Purpose-driven**: Every animation serves feedback (marked, winning, hovering)
- **Not overwhelming**: Glow animations loop once or twice; scale pops are one-off
- **60fps capable**: Simple transforms and opacity changes (GPU-accelerated)
- **No external libraries**: Pure CSS keyframes and transitions

### Typography Choices
- **System font stack**: Fast, accessible, familiar to users
- **Weight variation**: Bold for emphasis, regular for body; visual hierarchy clear
- **Letter-spacing**: Subtle increase on headings for playfulness without loss of readability
- **Text-shadow**: Soft purple shadow on titles adds depth and personality
- **No rotation or skew**: Keeps text readable while adding personality

---

## 7. Implementation Checklist

- [ ] Define CSS custom properties (variables) for all colors
- [ ] Add keyframe animations to stylesheet
- [ ] Create utility classes for colors, shadows, animations
- [ ] Update `base.html` for font stack and theme setup
- [ ] Redesign `home.html` (start screen) with hero styling
- [ ] Update `game_screen.html` header with new typography
- [ ] Refresh `bingo_board.html` with vibrant colors and marked square glow
- [ ] Enhance `bingo_modal.html` for celebratory feedback
- [ ] Test all interactions at 60fps (DevTools Performance)
- [ ] Verify accessibility (color contrast, keyboard navigation)
- [ ] Validate animations on mobile (smooth performance)

---

## 8. Color Reference Card

Quick hex copy-paste reference:

```
Primary: #7C3AED, #E9D5FF
Secondary: #14B8A6, #D1FAE5
Accent: #EC4899, #FBCFE8, #FBBF24, #FEF3C7, #F97316, #FFEDD5
Text: #1F2937, #4B5563, #F3F4F6, #FFFFFF
Background: #FAFAFA, #FFFFFF
Overlay: rgba(31, 41, 55, 0.85), rgba(255, 255, 255, 0.95)
```
