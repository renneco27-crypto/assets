import base64
import os
import re
import shutil

ROOT_DIR = r"c:\Users\yuze2\Documents\antigravity\radiant-oppenheimer"
DOWNLOADS_DIR = r"C:\Users\yuze2\Downloads"

# 1. Extract QR code base64 from slide-StudyUp-2026-11-01T19-34-17.html
slide_android_path = os.path.join(DOWNLOADS_DIR, "slide-StudyUp-2026-11-01T19-34-17.html")
with open(slide_android_path, "r", encoding="utf-8") as f:
    android_html = f.read()

qr_match = re.search(r'src="(data:image/png;base64,[^"]+)"', android_html)
QR_BASE64 = qr_match.group(1) if qr_match else ""

# 2. Load mascot base64 (with hat for the single featured mascot, and clean mascot)
with open(os.path.join(ROOT_DIR, "assets", "mascot_with_hat.png"), "rb") as f:
    MASCOT_HAT_B64 = "data:image/png;base64," + base64.b64encode(f.read()).decode("ascii")

with open(os.path.join(ROOT_DIR, "assets", "mascot_clean.png"), "rb") as f:
    MASCOT_CLEAN_B64 = "data:image/png;base64," + base64.b64encode(f.read()).decode("ascii")

AVATAR_URL = "https://lh3.googleusercontent.com/a/ACg8ocKYI4XjO8aibWhSSZVzJ3Hl8W7wIq2x5ehsRAmeNAAsfb5_I4zO=s96-c"

# Shared CSS & Design Tokens (99% our created Educational App UI design + 1% creativity + Notched Bottom Navbar)
SHARED_HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>__PAGE_TITLE__</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg-canvas: #e5e6eb;
      --coral: #eb7d57;
      --coral-dark: #e06842;
      --dark-indigo: #18152d;
      --deep-purple: #1b0e3f;
      --mid-purple: #5928c9;
      --soft-lavender: #d7d1f8;
      --surface-card: #ffffff;
      --surface-muted: #f6f5fb;
      --text-muted: #8b87a0;
    }

    * {
      box-sizing: border-box;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
      user-select: none;
    }

    body {
      margin: 0;
      padding: 0;
      background-color: var(--bg-canvas);
      background-image: radial-gradient(circle at 50% 25%, #f0f1f6 0%, #dcdfe7 100%);
      font-family: 'Plus Jakarta Sans', 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: flex-start;
      overflow-x: hidden;
      color: var(--dark-indigo);
    }

    /* Phone Frame Styling (99% Our Created Design System) */
    .phone-frame {
      width: 356px;
      height: 768px;
      background: #fafafe;
      border-radius: 38px;
      box-shadow:
        0 26px 54px -12px rgba(24, 21, 45, 0.16),
        0 8px 20px -4px rgba(24, 21, 45, 0.07),
        0 0 0 1px rgba(255, 255, 255, 0.95) inset;
      position: relative;
      overflow: hidden;
      flex-shrink: 0;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: transform 0.35s cubic-bezier(0.22, 1, 0.36, 1), box-shadow 0.35s ease;
    }

    .phone-frame.highlight-ring {
      box-shadow:
        0 30px 64px -10px rgba(89, 40, 201, 0.30),
        0 0 0 3px #eb7d57;
    }

    /* Signature Deep Royal Purple Wavy Header */
    .purple-wave-header {
      background: linear-gradient(155deg, #1b0e3f 0%, #311770 42%, #5928c9 78%, #6828e0 100%);
      position: relative;
      overflow: hidden;
    }

    /* Hero Banner Gradient */
    .hero-banner-bg {
      background: linear-gradient(125deg, #1b0f3e 0%, #2f1b63 52%, #5c37a0 100%);
      position: relative;
      overflow: hidden;
    }

    /* Active Coral Pill Glow */
    .pill-coral-active {
      background: linear-gradient(180deg, #f08562 0%, #e56d48 100%);
      color: #ffffff;
      border: 1px solid transparent;
      box-shadow: 0 7px 16px rgba(235, 125, 87, 0.44), 0 2px 5px rgba(235, 125, 87, 0.28);
    }

    .pill-outlined {
      background: #ffffff;
      color: #2c2647;
      border: 1.2px solid #e2e0ee;
      transition: all 0.2s ease;
    }

    .pill-outlined:hover {
      border-color: #5928c9;
      background: #f6f4fe;
    }

    /* Clean White Educational Cards */
    .edu-card {
      background: #ffffff;
      border: 1.2px solid #eceaf6;
      border-radius: 18px;
      box-shadow: 0 6px 18px rgba(24, 21, 45, 0.045);
      transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
    }

    .edu-card:hover {
      border-color: #d7d1f8;
      box-shadow: 0 10px 24px rgba(35, 22, 74, 0.08);
    }

    /* Soft Lavender Icon Badge */
    .badge-lavender {
      background: #ede9fe;
      color: #4c2bc2;
    }

    .badge-coral {
      background: #fff0eb;
      color: #e06842;
    }

    .badge-emerald {
      background: #e8fbf3;
      color: #0d9462;
    }

    /* Notched Bottom Navigation Bar (Matching Uploaded Reference Image) */
    .notched-navbar-wrap {
      position: relative;
      width: 100%;
      height: 82px;
      flex-shrink: 0;
      z-index: 30;
      margin-top: auto;
    }

    .notched-navbar-svg {
      position: absolute;
      bottom: 0;
      left: 0;
      width: 100%;
      height: 70px;
      filter: drop-shadow(0 -8px 20px rgba(24, 21, 45, 0.08));
      pointer-events: none;
    }

    .notched-fab {
      position: absolute;
      left: 50%;
      top: 0px;
      transform: translateX(-50%);
      width: 56px;
      height: 56px;
      border-radius: 9999px;
      background: linear-gradient(145deg, #f28865 0%, #e56b45 100%);
      box-shadow:
        0 8px 20px rgba(235, 125, 87, 0.48),
        0 2px 6px rgba(235, 125, 87, 0.30),
        0 0 0 3px #fafafe;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      color: #ffffff;
      cursor: pointer;
      z-index: 40;
    }

    .notched-nav-items {
      position: absolute;
      bottom: 0;
      left: 0;
      right: 0;
      height: 66px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 18px 8px 18px;
      z-index: 35;
    }

    .nav-tab-btn {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      gap: 3px;
      min-width: 54px;
      padding: 4px 2px;
      color: #8b87a0;
      cursor: pointer;
      transition: color 0.2s ease;
    }

    .nav-tab-btn.active {
      color: #23164a;
      font-weight: 700;
    }

    .nav-tab-btn.active svg {
      stroke: #eb7d57;
    }

    /* Home Indicator Bar */
    .home-indicator {
      position: absolute;
      bottom: 5px;
      left: 50%;
      transform: translateX(-50%);
      width: 116px;
      height: 4px;
      background-color: #18152d;
      opacity: 0.18;
      border-radius: 999px;
      z-index: 45;
      pointer-events: none;
    }

    .no-scrollbar::-webkit-scrollbar {
      display: none;
    }
    .no-scrollbar {
      -ms-overflow-style: none;
      scrollbar-width: none;
    }
  </style>
</head>
"""

def status_bar(dark=False):
    color = "#18152d" if dark else "#ffffff"
    opacity = "0.45" if dark else "0.5"
    return f"""
      <div class="flex items-center justify-between px-7 pt-3.5 pb-1.5" style="color: {color};">
        <span class="text-[13px] font-bold tracking-tight">9:41</span>
        <div class="flex items-center gap-1.5">
          <svg width="16" height="11" viewBox="0 0 16 11" fill="none">
            <rect x="0.5" y="7" width="2.6" height="3.5" rx="0.8" fill="{color}"/>
            <rect x="4.5" y="5" width="2.6" height="5.5" rx="0.8" fill="{color}"/>
            <rect x="8.5" y="2.8" width="2.6" height="7.7" rx="0.8" fill="{color}"/>
            <rect x="12.5" y="0.5" width="2.6" height="10" rx="0.8" fill="{color}"/>
          </svg>
          <svg width="15" height="11" viewBox="0 0 15 11" fill="none">
            <path d="M7.5 10.5C8.32843 10.5 9 9.82843 9 9C9 8.17157 8.32843 7.5 7.5 7.5C6.67157 7.5 6 8.17157 6 9C6 9.82843 6.67157 10.5 7.5 10.5Z" fill="{color}"/>
            <path d="M4.3 6.7C5.15 5.85 6.27 5.38 7.5 5.38C8.73 5.38 9.85 5.85 10.7 6.7" stroke="{color}" stroke-width="1.5" stroke-linecap="round"/>
            <path d="M1.8 4.1C3.33 2.57 5.35 1.72 7.5 1.72C9.65 1.72 11.67 2.57 13.2 4.1" stroke="{color}" stroke-width="1.5" stroke-linecap="round"/>
          </svg>
          <svg width="23" height="11" viewBox="0 0 23 11" fill="none">
            <rect x="0.5" y="1" width="19" height="9" rx="2.5" stroke="{color}" stroke-opacity="{opacity}"/>
            <rect x="2" y="2.5" width="16" height="6" rx="1.3" fill="{color}"/>
            <path d="M21 3.8V7.2C21.8 6.9 22.3 6.2 22.3 5.5C22.3 4.8 21.8 4.1 21 3.8Z" fill="{color}" fill-opacity="{opacity}"/>
          </svg>
        </div>
      </div>
"""

def bottom_navbar(active_tab="library", is_showcase=False):
    # Maps tabs to either showcase JS switcher or file links
    def nav_action(tab_num, filename):
        if is_showcase:
            return f"onclick=\"switchPhoneScreen({tab_num})\""
        return f"onclick=\"window.location.href='{filename}'\""

    lib_cls = "active" if active_tab == "library" else ""
    feed_cls = "active" if active_tab == "feed" else ""
    rank_cls = "active" if active_tab == "leaderboard" else ""
    app_cls = "active" if active_tab == "android" else ""

    return f"""
    <!-- Notched Bottom Navbar (Reference Image Style: 2 Left, Center Docked Circle Button, 2 Right) -->
    <div class="notched-navbar-wrap">
      <svg class="notched-navbar-svg" viewBox="0 0 356 70" preserveAspectRatio="none" fill="none">
        <path d="M 0,22 Q 0,0 22,0 L 118,0 C 136,0 142,38 178,38 C 214,38 220,0 238,0 L 334,0 Q 356,0 356,22 L 356,70 L 0,70 Z" fill="#ffffff"/>
        <path d="M 0,22 Q 0,0 22,0 L 118,0 C 136,0 142,38 178,38 C 214,38 220,0 238,0 L 334,0 Q 356,0 356,22" stroke="#eceaf6" stroke-width="1.2" fill="none"/>
      </svg>

      <!-- Center Circular Notch Button: Create Deck / Study Modes -->
      <button {nav_action(5, 'slide-StudyUp-2026-11-01T19-35-38.html')} class="notched-fab gsap-btn" title="Create Deck / Study Modes">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
          <path d="M5 12h14"/><path d="M12 5v14"/>
        </svg>
        <span class="text-[8.5px] font-bold tracking-tight leading-none mt-0.5">Create</span>
      </button>

      <div class="notched-nav-items">
        <!-- Left 2 Nav Items -->
        <div class="flex items-center gap-3">
          <button {nav_action(1, 'slide-StudyUp-2026-11-01T19-33-17.html')} class="nav-tab-btn {lib_cls} gsap-btn" title="My Library">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M15 21v-8a1 1 0 0 0-1-1h-4a1 1 0 0 0-1 1v8"/>
              <path d="M3 10a2 2 0 0 1 .709-1.528l7-6a2 2 0 0 1 2.582 0l7 6A2 2 0 0 1 21 10v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>
            </svg>
            <span class="text-[10px]">My Library</span>
          </button>

          <button {nav_action(2, 'slide-StudyUp-2026-11-01T19-33-39.html')} class="nav-tab-btn {feed_cls} gsap-btn" title="Public Feed">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <circle cx="12" cy="12" r="10"/>
              <path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"/>
              <path d="M2 12h20"/>
            </svg>
            <span class="text-[10px]">Public Feed</span>
          </button>
        </div>

        <!-- Center Spacer for Notch -->
        <div class="w-14 shrink-0"></div>

        <!-- Right 2 Nav Items -->
        <div class="flex items-center gap-3">
          <button {nav_action(3, 'slide-StudyUp-2026-11-01T19-33-49.html')} class="nav-tab-btn {rank_cls} gsap-btn" title="Leaderboard">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M10 14.66v1.626a2 2 0 0 1-.976 1.696A5 5 0 0 0 7 21.978"/>
              <path d="M14 14.66v1.626a2 2 0 0 0 .976 1.696A5 5 0 0 1 17 21.978"/>
              <path d="M18 9h1.5a1 1 0 0 0 0-5H18"/><path d="M4 22h16"/>
              <path d="M6 9a6 6 0 0 0 12 0V3a1 1 0 0 0-1-1H7a1 1 0 0 0-1 1z"/>
              <path d="M6 9H4.5a1 1 0 0 1 0-5H6"/>
            </svg>
            <span class="text-[10px]">Leaderboard</span>
          </button>

          <button {nav_action(4, 'slide-StudyUp-2026-11-01T19-34-17.html')} class="nav-tab-btn {app_cls} gsap-btn" title="Android App • Lawrence">
            <div class="relative">
              <img src="{AVATAR_URL}" alt="Lawrence" class="w-5 h-5 rounded-full object-cover border border-[#5928c9]" />
              <span class="absolute -bottom-0.5 -right-0.5 w-2 h-2 rounded-full bg-[#eb7d57] ring-1 ring-white"></span>
            </div>
            <span class="text-[10px]">Android App</span>
          </button>
        </div>
      </div>
      <div class="home-indicator"></div>
    </div>
"""

# ==============================================================================
# SCREEN 1: MY LIBRARY (Backbone from slide-StudyUp-2026-11-01T19-33-17.html)
# Progressive disclosure: Filter pills + collapsible deck list so user isn't
# overwhelmed; ONLY screen with the mascot (with hat) so mascot isn't spammed!
# ==============================================================================
def build_screen1_inner(is_showcase=False):
    deck_click = "onclick=\"switchPhoneScreen(5)\"" if is_showcase else "onclick=\"window.location.href='slide-StudyUp-2026-11-01T19-35-38.html'\""
    return f"""
    <section id="screen1" class="phone-frame">
      <div class="flex-1 overflow-y-auto no-scrollbar pb-3">
        <!-- Deep Royal Purple Wavy Header -->
        <div class="purple-wave-header pb-9">
          {status_bar(dark=False)}
          <!-- Decorative Concentric Circles (99% our design) -->
          <svg class="absolute inset-0 w-full h-full pointer-events-none" viewBox="0 0 356 210" fill="none">
            <circle cx="295" cy="95" r="110" fill="#462199" fill-opacity="0.35"/>
            <circle cx="295" cy="95" r="78" fill="#5e32c4" fill-opacity="0.40"/>
            <circle cx="295" cy="95" r="48" fill="#7747e3" fill-opacity="0.35"/>
          </svg>

          <!-- Top User Bar: StudyUp + Lawrence! + Server Status Pill -->
          <div class="relative z-10 px-6 pt-2 flex items-center justify-between">
            <div class="flex items-center gap-2.5">
              <img src="{AVATAR_URL}" alt="Google Account" class="w-9 h-9 rounded-full object-cover border-2 border-white/80 shadow-sm"/>
              <div>
                <div class="flex items-center gap-1.5">
                  <span class="text-white/80 text-[11px] font-bold uppercase tracking-wider">StudyUp</span>
                  <span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-[9.5px] font-semibold bg-white/15 text-rose-200 border border-white/15" title="Server Online • Extension Relay Worker is Closed / Disconnected">
                    <span class="w-1.5 h-1.5 rounded-full bg-rose-400 animate-pulse"></span>
                    Server Offline
                  </span>
                </div>
                <h1 class="text-white text-[19px] font-extrabold tracking-tight leading-tight">
                  Hi, Lawrence!
                </h1>
              </div>
            </div>
            <button class="gsap-btn w-9 h-9 rounded-full bg-white/15 hover:bg-white/25 flex items-center justify-center text-white border border-white/20" title="Sign out">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="m16 17 5-5-5-5"/><path d="M21 12H9"/><path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"/>
              </svg>
            </button>
          </div>

          <!-- Hero Welcome & Streak Summary inside Header (Single Purposeful Mascot with Hat!) -->
          <div class="relative z-10 px-6 pt-3.5 flex items-center justify-between">
            <div class="max-w-[190px]">
              <p class="text-[#d7d1f8] text-[11.5px] font-medium">My Library • Your decks &amp; study streaks</p>
              <div class="mt-2.5 flex items-center gap-2.5">
                <!-- Day Streak Pill -->
                <div class="bg-white/15 backdrop-blur-md border border-white/20 rounded-2xl px-3 py-1.5 flex items-center gap-2">
                  <span class="text-[#ffb443] text-base">🔥</span>
                  <div>
                    <div class="text-white text-[14px] font-extrabold leading-none">2 Days</div>
                    <div class="text-white/70 text-[9.5px]">Day streak</div>
                  </div>
                </div>
                <!-- Studied Today Pill -->
                <div class="bg-white/15 backdrop-blur-md border border-white/20 rounded-2xl px-3 py-1.5">
                  <div class="text-white text-[14px] font-extrabold leading-none">0</div>
                  <div class="text-white/70 text-[9.5px]">Studied today</div>
                </div>
              </div>
            </div>

            <!-- Single Mascot (With Graduation Cap Attached) - Not Repeated on Every Panel! -->
            <div id="mascot-screen1" class="mascot-interactive w-[112px] h-[112px] -mr-1 -mb-3 relative z-20 cursor-pointer select-none" title="StudyUp Mascot!">
              <img src="{MASCOT_HAT_B64}" alt="StudyUp Mascot with Hat" class="w-full h-full object-contain drop-shadow-[0_10px_16px_rgba(18,12,43,0.45)]"/>
            </div>
          </div>

          <!-- Layered White Wave Cutout at Bottom of Header -->
          <svg class="absolute bottom-0 left-0 w-full h-[28px] pointer-events-none" viewBox="0 0 356 28" preserveAspectRatio="none">
            <path d="M0,14 C95,32 245,-6 356,16 L356,28 L0,28 Z" fill="rgba(255,255,255,0.22)"/>
            <path d="M0,20 C115,34 235,0 356,21 L356,28 L0,28 Z" fill="#fafafe"/>
          </svg>
        </div>

        <!-- Progressive Disclosure Filter Bar (Hick's Law: Chunking 4 Decks by Category) -->
        <div class="px-5 pt-2 pb-3 flex items-center justify-between gap-1.5 overflow-x-auto no-scrollbar">
          <button onclick="filterLibraryDecks('all', this)" class="lib-filter-btn gsap-btn pill-coral-active px-3.5 py-1.5 rounded-full text-[11.5px] font-bold shrink-0">
            All Decks (4)
          </button>
          <button onclick="filterLibraryDecks('active', this)" class="lib-filter-btn gsap-btn pill-outlined px-3 py-1.5 rounded-full text-[11.5px] font-semibold shrink-0">
            Active Streak (2)
          </button>
          <button onclick="filterLibraryDecks('cs', this)" class="lib-filter-btn gsap-btn pill-outlined px-3 py-1.5 rounded-full text-[11.5px] font-semibold shrink-0">
            CS &amp; Science (2)
          </button>
        </div>

        <!-- My Library Decks Backbone List -->
        <div id="libraryDecksList" class="px-5 space-y-2.5">
          <!-- Deck 1: Hci midtermasfdjwgjkfgsjgjgjdjfgdf -->
          <div data-cat="active" class="deck-item edu-card p-3.5 cursor-pointer" {deck_click}>
            <div class="flex items-start justify-between gap-2.5">
              <div class="w-10 h-10 rounded-2xl badge-lavender flex items-center justify-center shrink-0 font-extrabold text-xs">
                HCI
              </div>
              <div class="flex-1 min-w-0">
                <div class="flex items-center gap-1.5 flex-wrap">
                  <span class="badge-emerald px-2 py-0.5 rounded-full text-[10px] font-bold">Study Notes</span>
                  <span class="badge-coral px-2 py-0.5 rounded-full text-[10px] font-bold">🔥 2 days Streak</span>
                </div>
                <h3 class="text-[13.5px] font-extrabold text-[#18152d] truncate mt-1" title="Hci midtermasfdjwgjkfgsjgjgjdjfgdf">
                  Hci midtermasfdjwgjkfgsjgjgjdjfgdf
                </h3>
                <div class="flex items-center gap-2.5 text-[11px] text-[#8b87a0] mt-0.5">
                  <span class="font-semibold text-[#5928c9]">155 cards</span>
                  <span>•</span>
                  <span>Last studied: 11/1/2026</span>
                </div>
              </div>
              <span class="gsap-btn px-2.5 py-1.5 rounded-xl bg-[#ede9fe] text-[#5928c9] text-[11px] font-bold shrink-0">
                Resume →
              </span>
            </div>
            <!-- Progress + Secondary Actions (Export DOCX / Delete) -->
            <div class="mt-2.5 pt-2 border-t border-slate-100 flex items-center justify-between">
              <div class="w-36 h-1.5 bg-[#eceaf6] rounded-full overflow-hidden">
                <div class="h-full bg-[#eb7d57] rounded-full" style="width: 12%;"></div>
              </div>
              <div class="flex items-center gap-1.5" onclick="event.stopPropagation();">
                <button class="gsap-btn p-1 text-[#8b87a0] hover:text-[#5928c9] rounded-lg" title="Export deck as DOCX">
                  <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 15V3"/><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><path d="m7 10 5 5 5-5"/></svg>
                </button>
                <button class="gsap-btn p-1 text-[#8b87a0] hover:text-rose-500 rounded-lg" title="Delete deck">
                  <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M10 11v6"/><path d="M14 11v6"/><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6"/><path d="M3 6h18"/><path d="M8 6V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/></svg>
                </button>
              </div>
            </div>
          </div>

          <!-- Deck 2: Sample Deck: Motion Basics and Python Loops -->
          <div data-cat="active" class="deck-item edu-card p-3.5 cursor-pointer" {deck_click}>
            <div class="flex items-start justify-between gap-2.5">
              <div class="w-10 h-10 rounded-2xl badge-coral flex items-center justify-center shrink-0 font-extrabold text-xs">
                PY
              </div>
              <div class="flex-1 min-w-0">
                <div class="flex items-center gap-1.5 flex-wrap">
                  <span class="badge-lavender px-2 py-0.5 rounded-full text-[10px] font-bold">Mixed Sample</span>
                  <span class="badge-coral px-2 py-0.5 rounded-full text-[10px] font-bold">🔥 2 days Streak</span>
                </div>
                <h3 class="text-[13.5px] font-extrabold text-[#18152d] truncate mt-1">
                  Sample Deck: Motion Basics and Python Loops
                </h3>
                <div class="flex items-center gap-2.5 text-[11px] text-[#8b87a0] mt-0.5">
                  <span class="font-semibold text-[#5928c9]">17 cards</span>
                  <span>•</span>
                  <span>Last studied: 11/1/2026</span>
                </div>
              </div>
              <span class="gsap-btn px-2.5 py-1.5 rounded-xl bg-[#fff0eb] text-[#e06842] text-[11px] font-bold shrink-0">
                Resume →
              </span>
            </div>
          </div>

          <!-- Progressive Disclosure Drawer for Remaining 2 Decks (Avoids visual overload) -->
          <div id="moreDecksContainer" class="hidden space-y-2.5">
            <!-- Deck 3: Elementary Sciences -->
            <div data-cat="cs" class="deck-item edu-card p-3.5 cursor-pointer" {deck_click}>
              <div class="flex items-start justify-between gap-2.5">
                <div class="w-10 h-10 rounded-2xl badge-emerald flex items-center justify-center shrink-0 font-extrabold text-xs">
                  SCI
                </div>
                <div class="flex-1 min-w-0">
                  <span class="badge-emerald px-2 py-0.5 rounded-full text-[10px] font-bold">math coding butterfly notes</span>
                  <h3 class="text-[13px] font-extrabold text-[#18152d] line-clamp-1 mt-1">
                    Elementary Sciences: Mathematics, Coding Basics, and Butterfly Biology
                  </h3>
                  <div class="text-[11px] text-[#8b87a0] mt-0.5 font-semibold">24 cards</div>
                </div>
                <span class="gsap-btn px-2.5 py-1.5 rounded-xl bg-[#ede9fe] text-[#5928c9] text-[11px] font-bold shrink-0">
                  Resume →
                </span>
              </div>
            </div>

            <!-- Deck 4: JavaScript Data Structure Algorithm -->
            <div data-cat="cs" class="deck-item edu-card p-3.5 cursor-pointer" {deck_click}>
              <div class="flex items-start justify-between gap-2.5">
                <div class="w-10 h-10 rounded-2xl badge-lavender flex items-center justify-center shrink-0 font-extrabold text-xs">
                  JS
                </div>
                <div class="flex-1 min-w-0">
                  <span class="badge-lavender px-2 py-0.5 rounded-full text-[10px] font-bold">JavaScript Data Structure Algorithm</span>
                  <h3 class="text-[13px] font-extrabold text-[#18152d] truncate mt-1">
                    JavaScript Data Structure Algorithm
                  </h3>
                  <div class="text-[11px] text-[#8b87a0] mt-0.5 font-semibold">59 cards</div>
                </div>
                <span class="gsap-btn px-2.5 py-1.5 rounded-xl bg-[#ede9fe] text-[#5928c9] text-[11px] font-bold shrink-0">
                  Resume →
                </span>
              </div>
            </div>
          </div>

          <button id="toggleMoreDecksBtn" onclick="toggleMoreDecks()" class="gsap-btn w-full py-2 rounded-2xl border border-dashed border-[#c7bfe8] text-[11.5px] font-bold text-[#5928c9] hover:bg-[#f3f0ff] transition-colors">
            Show 2 More Decks (Elementary Sciences &amp; JS) ↓
          </button>
        </div>
      </div>

      {bottom_navbar(active_tab="library", is_showcase=is_showcase)}
    </section>
"""

# ==============================================================================
# SCREEN 2: PUBLIC FEED (Backbone from slide-StudyUp-2026-11-01T19-33-39.html)
# No repeated mascot! Uses our purple wavy header, coral/lavender pills, and
# clean progressive-disclosure action drawer for Merge/Categorize.
# ==============================================================================
def build_screen2_inner(is_showcase=False):
    back_action = "onclick=\"switchPhoneScreen(1)\"" if is_showcase else "onclick=\"window.location.href='slide-StudyUp-2026-11-01T19-33-17.html'\""
    open_action = "onclick=\"switchPhoneScreen(5)\"" if is_showcase else "onclick=\"window.location.href='slide-StudyUp-2026-11-01T19-35-38.html'\""
    return f"""
    <section id="screen2" class="phone-frame">
      <div class="flex-1 overflow-y-auto no-scrollbar pb-3">
        <!-- Deep Royal Purple Wavy Header -->
        <div class="purple-wave-header pb-8">
          {status_bar(dark=False)}
          <div class="relative z-10 px-6 pt-2 flex items-center gap-3">
            <button {back_action} class="gsap-btn w-8 h-8 rounded-full bg-white/15 text-white flex items-center justify-center border border-white/20">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="m12 19-7-7 7-7"/><path d="M19 12H5"/></svg>
            </button>
            <div>
              <h1 class="text-white text-[20px] font-extrabold tracking-tight leading-tight">Public Feed</h1>
              <p class="text-[#d7d1f8] text-[11.5px] font-medium">Community-shared decks</p>
            </div>
          </div>

          <!-- Search Input Inside Header -->
          <div class="relative z-10 px-6 pt-3.5">
            <div class="relative">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#8b87a0" stroke-width="2" class="absolute left-3.5 top-1/2 -translate-y-1/2 pointer-events-none">
                <path d="m21 21-4.34-4.34"/><circle cx="11" cy="11" r="8"/>
              </svg>
              <input id="feedSearchInput" oninput="filterFeedCard(this.value)" type="text" placeholder="Search decks by title, subject, or author..." class="w-full pl-10 pr-4 py-2.5 rounded-2xl bg-white text-[12px] text-[#18152d] placeholder-[#8b87a0] font-medium shadow-md focus:outline-none focus:ring-2 focus:ring-[#eb7d57]" />
            </div>
          </div>

          <svg class="absolute bottom-0 left-0 w-full h-[24px] pointer-events-none" viewBox="0 0 356 24" preserveAspectRatio="none">
            <path d="M0,12 C110,28 240,-4 356,14 L356,24 L0,24 Z" fill="#fafafe"/>
          </svg>
        </div>

        <!-- Folder Filter Pills Backbone: All, maee (0), Lawrence (0), + New Folder -->
        <div class="px-5 pt-2 pb-3 flex items-center gap-1.5 overflow-x-auto no-scrollbar">
          <button onclick="selectFolderPill(this)" class="folder-pill gsap-btn pill-coral-active px-3 py-1.5 rounded-full text-[11px] font-bold flex items-center gap-1 shrink-0">
            <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M12 7v14"/><path d="M3 18a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1h5a4 4 0 0 1 4 4 4 4 0 0 1 4-4h5a1 1 0 0 1 1 1v13a1 1 0 0 1-1 1h-6a3 3 0 0 0-3 3 3 3 0 0 0-3-3z"/></svg>
            All
          </button>
          <button onclick="selectFolderPill(this)" class="folder-pill gsap-btn pill-outlined px-3 py-1.5 rounded-full text-[11px] font-semibold flex items-center gap-1 shrink-0">
            <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m6 14 1.5-2.9A2 2 0 0 1 9.24 10H20a2 2 0 0 1 1.94 2.5l-1.54 6a2 2 0 0 1-1.95 1.5H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h3.9a2 2 0 0 1 1.69.9l.81 1.2a2 2 0 0 0 1.67.9H18a2 2 0 0 1 2 2v2"/></svg>
            maee <span class="opacity-60">(0)</span>
          </button>
          <button onclick="selectFolderPill(this)" class="folder-pill gsap-btn pill-outlined px-3 py-1.5 rounded-full text-[11px] font-semibold flex items-center gap-1 shrink-0">
            <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m6 14 1.5-2.9A2 2 0 0 1 9.24 10H20a2 2 0 0 1 1.94 2.5l-1.54 6a2 2 0 0 1-1.95 1.5H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h3.9a2 2 0 0 1 1.69.9l.81 1.2a2 2 0 0 0 1.67.9H18a2 2 0 0 1 2 2v2"/></svg>
            Lawrence <span class="opacity-60">(0)</span>
          </button>
          <button class="gsap-btn px-2.5 py-1.5 rounded-full border border-dashed border-[#eb7d57] text-[#e06842] text-[11px] font-bold flex items-center gap-1 shrink-0">
            + New Folder
          </button>
        </div>

        <!-- Community Shared Deck Card Backbone -->
        <div class="px-5 space-y-3">
          <div id="publicDeckCard" class="edu-card p-4">
            <div class="flex items-start gap-3">
              <button onclick="this.classList.toggle('bg-[#5928c9]'); this.classList.toggle('text-white');" class="gsap-btn mt-0.5 w-6 h-6 rounded-lg border border-[#d7d1f8] bg-[#f6f5fb] flex items-center justify-center text-transparent shrink-0" title="Select deck to merge">
                ✓
              </button>
              <div class="flex-1 min-w-0">
                <div class="flex items-center gap-1.5 flex-wrap">
                  <span class="badge-lavender px-2.5 py-0.5 rounded-full text-[10px] font-bold">Mixed Sample</span>
                  <span class="text-[10.5px] text-[#8b87a0] font-medium">10/29/2026</span>
                </div>
                <h3 class="text-[14.5px] font-extrabold text-[#18152d] leading-snug mt-1.5" title="Double-click to rename">
                  Sample Deck: Motion Basics and Python Loops
                </h3>
                <div class="flex items-center gap-3 mt-1.5 text-[11.5px] text-[#8b87a0]">
                  <span class="font-semibold text-[#2c2647]">by Lawrence Cortes</span>
                  <span>•</span>
                  <span class="text-[#0d9462] font-bold">7 downloads</span>
                </div>
              </div>
            </div>

            <!-- Primary CTA + Progressive Disclosure for Deck Tools (Merge / Categorize / Delete) -->
            <div class="mt-4 pt-3 border-t border-slate-100 flex items-center justify-between gap-2">
              <button {open_action} class="gsap-btn pill-coral-active px-4 py-2 rounded-xl text-[12px] font-bold flex items-center gap-1.5">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M12 7v14"/><path d="M3 18a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1h5a4 4 0 0 1 4 4 4 4 0 0 1 4-4h5a1 1 0 0 1 1 1v13a1 1 0 0 1-1 1h-6a3 3 0 0 0-3 3 3 3 0 0 0-3-3z"/></svg>
                Open project
              </button>

              <div class="flex items-center gap-1.5">
                <button class="gsap-btn px-2.5 py-1.5 rounded-xl bg-[#f6f5fb] hover:bg-[#ede9fe] text-[#2c2647] text-[11px] font-semibold flex items-center gap-1 border border-[#eceaf6]" title="Merge with another deck">
                  <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12.83 2.18a2 2 0 0 0-1.66 0L2.6 6.08a1 1 0 0 0 0 1.83l8.58 3.91a2 2 0 0 0 1.66 0l8.58-3.9a1 1 0 0 0 0-1.83z"/><path d="M2 12a1 1 0 0 0 .58.91l8.6 3.91a2 2 0 0 0 1.65 0l8.58-3.9A1 1 0 0 0 22 12"/></svg>
                  Merge
                </button>
                <button class="gsap-btn px-2.5 py-1.5 rounded-xl bg-[#f6f5fb] hover:bg-[#ede9fe] text-[#2c2647] text-[11px] font-semibold flex items-center gap-1 border border-[#eceaf6]" title="Categorize deck">
                  <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 20a2 2 0 0 0 2-2V8a2 2 0 0 0-2-2h-7.9a2 2 0 0 1-1.69-.9L9.6 3.9A2 2 0 0 0 7.93 3H4a2 2 0 0 0-2 2v13a2 2 0 0 0 2 2Z"/></svg>
                  Categorize
                </button>
                <button class="gsap-btn p-1.5 rounded-xl bg-rose-50 text-rose-500 hover:bg-rose-100" title="Delete deck">
                  <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M10 11v6"/><path d="M14 11v6"/><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6"/><path d="M3 6h18"/></svg>
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>

      {bottom_navbar(active_tab="feed", is_showcase=is_showcase)}
    </section>
"""

# ==============================================================================
# SCREEN 3: LEADERBOARD (Backbone from slide-StudyUp-2026-11-01T19-33-49.html)
# No repeated mascot! Uses our royal purple card & coral pills.
# ==============================================================================
def build_screen3_inner(is_showcase=False):
    return f"""
    <section id="screen3" class="phone-frame">
      <div class="flex-1 overflow-y-auto no-scrollbar pb-3">
        <!-- Deep Royal Purple Wavy Header -->
        <div class="purple-wave-header pb-8">
          {status_bar(dark=False)}
          <div class="relative z-10 px-6 pt-2 flex items-center justify-between">
            <div>
              <div class="flex items-center gap-2">
                <h1 class="text-white text-[21px] font-extrabold tracking-tight">Leaderboard</h1>
                <span class="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full bg-white/15 text-[#ffb443] text-[10px] font-bold border border-white/20">
                  🔥 3-Day Rule
                </span>
              </div>
              <p class="text-[#d7d1f8] text-[11.5px] font-medium mt-0.5">
                Real-time rankings across global study sessions
              </p>
            </div>
          </div>

          <!-- Segmented Metric Switcher: Streak | Mastery | Score -->
          <div class="relative z-10 px-6 pt-3.5">
            <div class="bg-white/15 backdrop-blur-md p-1 rounded-2xl flex items-center border border-white/20">
              <button onclick="switchRankTab('Streak', '2d', this)" class="rank-mode-btn gsap-btn flex-1 py-1.5 rounded-xl pill-coral-active text-[11.5px] font-bold flex items-center justify-center gap-1">
                🔥 Streak
              </button>
              <button onclick="switchRankTab('Mastery', '94%', this)" class="rank-mode-btn gsap-btn flex-1 py-1.5 rounded-xl text-white/80 hover:text-white text-[11.5px] font-semibold flex items-center justify-center gap-1">
                ✨ Mastery
              </button>
              <button onclick="switchRankTab('Score', '1,420', this)" class="rank-mode-btn gsap-btn flex-1 py-1.5 rounded-xl text-white/80 hover:text-white text-[11.5px] font-semibold flex items-center justify-center gap-1">
                🎯 Score
              </button>
            </div>
          </div>

          <svg class="absolute bottom-0 left-0 w-full h-[24px] pointer-events-none" viewBox="0 0 356 24" preserveAspectRatio="none">
            <path d="M0,12 C110,28 240,-4 356,14 L356,24 L0,24 Z" fill="#fafafe"/>
          </svg>
        </div>

        <div class="px-5 pt-2 space-y-3.5">
          <!-- Featured Your Rank Card (99% Our Dark Royal Purple Card Style) -->
          <div class="hero-banner-bg rounded-[22px] p-4 text-white shadow-lg flex items-center justify-between relative overflow-hidden">
            <svg class="absolute inset-0 w-full h-full pointer-events-none" viewBox="0 0 316 96" fill="none">
              <circle cx="275" cy="48" r="65" fill="#4c2d8f" fill-opacity="0.45"/>
              <circle cx="275" cy="48" r="40" fill="#6441ad" fill-opacity="0.45"/>
            </svg>

            <div class="relative z-10 flex items-center gap-3.5">
              <div class="relative">
                <img src="{AVATAR_URL}" alt="Lawrence Cortes" class="w-13 h-13 w-[52px] h-[52px] rounded-2xl object-cover border-2 border-[#eb7d57] shadow-md"/>
                <span class="absolute -bottom-1 -right-1 px-1.5 py-0.5 rounded-full bg-[#eb7d57] text-[9px] font-extrabold uppercase text-white shadow">
                  You
                </span>
              </div>
              <div>
                <div class="flex items-center gap-1.5">
                  <span class="text-[#d7d1f8] text-[10px] font-bold uppercase tracking-wider">Your Rank</span>
                  <span class="px-2 py-0.5 rounded-full bg-amber-400/20 text-amber-300 text-[12px] font-extrabold">#1</span>
                </div>
                <p class="text-white text-[15px] font-extrabold mt-0.5">Lawrence Cortes</p>
              </div>
            </div>

            <div class="relative z-10 text-right">
              <p id="rankMetricLabel" class="text-[#d7d1f8] text-[10px] uppercase font-bold tracking-wider">Day Streak</p>
              <div class="flex items-center justify-end gap-1 text-[24px] font-extrabold text-[#ffb443] leading-tight">
                <span>🔥</span>
                <span id="rankMetricValue">2d</span>
              </div>
            </div>
          </div>

          <!-- Global Rankings List Backbone -->
          <div class="edu-card overflow-hidden">
            <div class="px-4 py-2.5 bg-[#f6f5fb] border-b border-[#eceaf6] flex items-center justify-between text-[11px] font-bold text-[#8b87a0] uppercase tracking-wider">
              <span>Rank &amp; Learner</span>
              <span id="tableMetricHeader">Streak</span>
            </div>
            <div class="divide-y divide-[#eceaf6]">
              <!-- Row 1: Law****ce Cor**s (You) -->
              <div class="px-4 py-3.5 flex items-center justify-between bg-[#faf8ff] border-l-4 border-l-[#eb7d57]">
                <div class="flex items-center gap-3 min-w-0">
                  <span class="w-6 h-6 rounded-full bg-amber-100 text-amber-700 font-extrabold text-[12px] flex items-center justify-center shrink-0">
                    1
                  </span>
                  <img src="{AVATAR_URL}" alt="Lawrence" class="w-8 h-8 rounded-full object-cover border border-[#d7d1f8] shrink-0"/>
                  <div class="min-w-0 flex items-center gap-1.5">
                    <span class="text-[13px] font-bold text-[#18152d] truncate">Law****ce Cor**s</span>
                    <span class="px-1.5 py-0.5 rounded-md bg-[#eb7d57] text-white text-[9px] font-extrabold uppercase">You</span>
                  </div>
                </div>
                <span id="row1MetricVal" class="text-[13.5px] font-extrabold text-[#e06842] flex items-center gap-1 shrink-0">
                  🔥 2d
                </span>
              </div>
            </div>
          </div>
        </div>
      </div>

      {bottom_navbar(active_tab="leaderboard", is_showcase=is_showcase)}
    </section>
"""

# ==============================================================================
# SCREEN 4: ANDROID APP (Backbone from slide-StudyUp-2026-11-01T19-34-17.html)
# Progressive disclosure: 2 clean tabs ("QR & APK Install" vs "Features & Setup")
# so the user isn't hit with QR + 4 feature cards + 3 setup steps all at once!
# ==============================================================================
def build_screen4_inner(is_showcase=False):
    back_action = "onclick=\"switchPhoneScreen(1)\"" if is_showcase else "onclick=\"window.location.href='slide-StudyUp-2026-11-01T19-33-17.html'\""
    return f"""
    <section id="screen4" class="phone-frame">
      <div class="flex-1 overflow-y-auto no-scrollbar pb-3">
        <!-- Deep Royal Purple Wavy Header -->
        <div class="purple-wave-header pb-8">
          {status_bar(dark=False)}
          <div class="relative z-10 px-6 pt-2 flex items-center justify-between">
            <button {back_action} class="gsap-btn inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-white/15 text-white text-[11px] font-bold border border-white/20">
              <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="m12 19-7-7 7-7"/><path d="M19 12H5"/></svg>
              Back to StudyUp
            </button>
            <span class="px-2.5 py-0.5 rounded-full bg-[#eb7d57]/25 text-[#ffb49a] text-[10px] font-bold border border-[#eb7d57]/40">
              Mobile Study Experience
            </span>
          </div>

          <div class="relative z-10 px-6 pt-3">
            <h1 class="text-white text-[19px] font-extrabold leading-tight tracking-tight">
              Study Anywhere with <span class="text-[#ff9c7a]">StudyUp Android</span>
            </h1>
            <p class="text-[#d7d1f8] text-[11px] leading-relaxed mt-1">
              Full offline active recall, math solver, and coding lab on the go.
            </p>
          </div>

          <svg class="absolute bottom-0 left-0 w-full h-[24px] pointer-events-none" viewBox="0 0 356 24" preserveAspectRatio="none">
            <path d="M0,12 C110,28 240,-4 356,14 L356,24 L0,24 Z" fill="#fafafe"/>
          </svg>
        </div>

        <!-- Progressive Disclosure Switcher (Prevents dumping QR + 4 Features + 3 Steps at once) -->
        <div class="px-5 pt-1.5 pb-3 flex items-center gap-2">
          <button onclick="switchAndroidTab('qr', this)" class="android-tab-btn gsap-btn flex-1 py-1.5 rounded-full pill-coral-active text-[11.5px] font-bold">
            1. Quick Scan &amp; APK
          </button>
          <button onclick="switchAndroidTab('features', this)" class="android-tab-btn gsap-btn flex-1 py-1.5 rounded-full pill-outlined text-[11.5px] font-semibold">
            2. Features &amp; 3-Step Setup
          </button>
        </div>

        <!-- TAB A: Quick Scan QR & Direct APK Download -->
        <div id="androidTabQR" class="px-5 space-y-3">
          <div class="edu-card p-4 text-center flex flex-col items-center">
            <span class="badge-coral px-2.5 py-0.5 rounded-full text-[10px] font-extrabold uppercase tracking-wider">Quick Scan</span>
            <h2 class="text-[15px] font-extrabold text-[#18152d] mt-1">Install on Your Phone</h2>

            <div class="my-3 p-2.5 bg-white rounded-2xl border-2 border-[#eceaf6] shadow-sm">
              <img src="{QR_BASE64}" alt="Scan to download StudyUp for Android" class="w-36 h-36 object-contain rounded-lg"/>
            </div>

            <p class="text-[11px] text-[#8b87a0] mb-3">
              Point your phone camera or Google Lens at the QR code
            </p>

            <a href="/api/download/apk" download="app-release.apk" class="gsap-btn w-full py-2.5 px-4 rounded-2xl pill-coral-active text-[12.5px] font-bold flex items-center justify-center gap-2">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M12 15V3"/><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><path d="m7 10 5 5 5-5"/></svg>
              Download APK Directly
            </a>
          </div>

          <div class="edu-card p-3 flex items-center justify-between">
            <div>
              <div class="text-[10px] font-extrabold uppercase text-[#5928c9]">Crafted by Lawrence Cortes</div>
              <div class="text-[10.5px] text-[#8b87a0]">Verified package • No telemetry</div>
            </div>
            <a href="https://dev.lawrencecortes.flashhub.net/" target="_blank" rel="noopener noreferrer" class="gsap-btn px-3 py-1.5 rounded-xl badge-lavender text-[11px] font-bold">
              Creator Webpage ↗
            </a>
          </div>
        </div>

        <!-- TAB B: 4 Feature Cards & Easy 3-Step Setup (Progressive Disclosure) -->
        <div id="androidTabFeatures" class="hidden px-5 space-y-2.5">
          <div class="grid grid-cols-2 gap-2.5">
            <div class="edu-card p-3">
              <div class="w-7 h-7 rounded-xl badge-coral flex items-center justify-center font-bold text-xs mb-1.5">⚡</div>
              <h3 class="text-[12px] font-extrabold text-[#18152d]">100% Offline Ready</h3>
              <p class="text-[10px] text-[#8b87a0] leading-snug mt-0.5">Flashcards &amp; progress stored with zero latency.</p>
            </div>
            <div class="edu-card p-3">
              <div class="w-7 h-7 rounded-xl badge-lavender flex items-center justify-center font-bold text-xs mb-1.5">🧮</div>
              <h3 class="text-[12px] font-extrabold text-[#18152d]">Math Step Solver</h3>
              <p class="text-[10px] text-[#8b87a0] leading-snug mt-0.5">Interactive step animations &amp; fraction cancellations.</p>
            </div>
            <div class="edu-card p-3">
              <div class="w-7 h-7 rounded-xl badge-lavender flex items-center justify-center font-bold text-xs mb-1.5">💻</div>
              <h3 class="text-[12px] font-extrabold text-[#18152d]">Mobile Coding Lab</h3>
              <p class="text-[10px] text-[#8b87a0] leading-snug mt-0.5">Compare Python, Java &amp; JS syntax with bug fixes.</p>
            </div>
            <div class="edu-card p-3">
              <div class="w-7 h-7 rounded-xl badge-emerald flex items-center justify-center font-bold text-xs mb-1.5">🎙️</div>
              <h3 class="text-[12px] font-extrabold text-[#18152d]">Voice Transcriber</h3>
              <p class="text-[10px] text-[#8b87a0] leading-snug mt-0.5">Hands-free oral active recall speech recognition.</p>
            </div>
          </div>

          <div class="edu-card p-3.5">
            <h3 class="text-[11px] font-extrabold uppercase tracking-wider text-[#5928c9] mb-2">Easy 3-Step Setup</h3>
            <div class="space-y-1.5 text-[11px]">
              <div class="flex items-center gap-2"><span class="font-extrabold text-[#eb7d57]">01. Download</span><span class="text-[#8b87a0]">— Scan QR or tap Download button.</span></div>
              <div class="flex items-center gap-2"><span class="font-extrabold text-[#eb7d57]">02. Open File</span><span class="text-[#8b87a0]">— Tap notification in browser/Files.</span></div>
              <div class="flex items-center gap-2"><span class="font-extrabold text-[#eb7d57]">03. Install</span><span class="text-[#8b87a0]">— Launch StudyUp with offline storage.</span></div>
            </div>
          </div>
        </div>
      </div>

      {bottom_navbar(active_tab="android", is_showcase=is_showcase)}
    </section>
"""

# ==============================================================================
# SCREEN 5: DECK DETAIL & STUDY MODES (Backbone from slide-StudyUp-2026-11-01T19-35-38.html)
# Progressive disclosure: Filters the 10 study modes into 3 clean categories
# ("Recall (4)", "Read & Media (3)", "Labs & Stats (3)") so user isn't hit with 10 boxes!
# ==============================================================================
def build_screen5_inner(is_showcase=False):
    back_action = "onclick=\"switchPhoneScreen(1)\"" if is_showcase else "onclick=\"window.location.href='slide-StudyUp-2026-11-01T19-33-17.html'\""
    return f"""
    <section id="screen5" class="phone-frame">
      <div class="flex-1 overflow-y-auto no-scrollbar pb-3">
        <!-- Deep Royal Purple Wavy Header -->
        <div class="purple-wave-header pb-8">
          {status_bar(dark=False)}
          <!-- Top Bar: Back + Deck Title + Export DOCX -->
          <div class="relative z-10 px-6 pt-2 flex items-center justify-between gap-2">
            <button {back_action} class="gsap-btn w-8 h-8 rounded-full bg-white/15 text-white flex items-center justify-center border border-white/20 shrink-0" aria-label="Go back">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="m12 19-7-7 7-7"/><path d="M19 12H5"/></svg>
            </button>
            <div class="flex-1 min-w-0">
              <div class="flex items-center gap-1.5">
                <span class="px-2 py-0.5 rounded-full bg-white/15 text-[#d7d1f8] text-[9.5px] font-bold">Study Notes</span>
                <span class="px-2 py-0.5 rounded-full bg-[#eb7d57]/30 text-[#ffb49a] text-[9.5px] font-bold">🔥 2d Streak</span>
              </div>
              <h1 class="text-white text-[15px] font-extrabold truncate mt-0.5" title="Hci midtermasfdjwgjkfgsjgjgjdjfgdf">
                Hci midtermasfdjwgjkfgsjgjgjdjfgdf
              </h1>
            </div>
            <button class="gsap-btn w-8 h-8 rounded-full bg-white/15 text-white flex items-center justify-center border border-white/20 shrink-0" title="Export deck as DOCX">
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 15V3"/><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><path d="m7 10 5 5 5-5"/></svg>
            </button>
          </div>

          <!-- Progress Ring + Mastery Pills + Edit/Publish Buttons -->
          <div class="relative z-10 px-6 pt-3 flex items-center justify-between gap-3">
            <div class="flex items-center gap-3">
              <div class="relative w-14 h-14 flex items-center justify-center">
                <svg width="56" height="56" class="transform -rotate-90">
                  <circle cx="28" cy="28" r="23" stroke="rgba(255,255,255,0.18)" stroke-width="5" fill="none"/>
                  <circle cx="28" cy="28" r="23" stroke="#eb7d57" stroke-width="5" fill="none" stroke-dasharray="35 145" stroke-linecap="round"/>
                </svg>
                <span class="absolute text-white text-[11px] font-extrabold">23%</span>
              </div>
              <div class="space-y-1 text-[10px] font-bold">
                <div class="px-2 py-0.5 rounded-full bg-emerald-400/20 text-emerald-200">0 Mastered</div>
                <div class="px-2 py-0.5 rounded-full bg-amber-400/20 text-amber-200">1 Learning</div>
                <div class="px-2 py-0.5 rounded-full bg-white/15 text-white">154 New</div>
              </div>
            </div>

            <div class="flex flex-col gap-1.5">
              <button class="gsap-btn px-3 py-1.5 rounded-xl bg-white text-[#23164a] text-[11px] font-extrabold shadow-sm">
                + Edit / Add Cards
              </button>
              <button class="gsap-btn px-3 py-1.5 rounded-xl bg-white/15 text-white border border-white/20 text-[11px] font-bold">
                Publish Deck
              </button>
            </div>
          </div>

          <svg class="absolute bottom-0 left-0 w-full h-[24px] pointer-events-none" viewBox="0 0 356 24" preserveAspectRatio="none">
            <path d="M0,12 C110,28 240,-4 356,14 L356,24 L0,24 Z" fill="#fafafe"/>
          </svg>
        </div>

        <!-- Due for Review Banner -->
        <div class="px-5 pt-1">
          <div class="edu-card p-3 border-l-4 border-l-[#eb7d57] flex items-center justify-between bg-[#fff9f6]">
            <div class="flex items-center gap-2">
              <span class="text-[#eb7d57]">🔔</span>
              <span class="text-[12px] font-bold text-[#18152d]">155 cards due for review today</span>
            </div>
            <button class="gsap-btn text-[11.5px] font-extrabold text-[#e06842] hover:underline shrink-0">
              Start review →
            </button>
          </div>
        </div>

        <!-- Progressive Disclosure Category Tabs for the 10 Study Modes (Hick's & Miller's Law) -->
        <div class="px-5 pt-3 pb-2 flex items-center justify-between gap-1.5">
          <button onclick="filterStudyModes('recall', this)" class="mode-cat-btn gsap-btn pill-coral-active px-3 py-1 rounded-full text-[11px] font-bold">
            Active Recall (4)
          </button>
          <button onclick="filterStudyModes('content', this)" class="mode-cat-btn gsap-btn pill-outlined px-3 py-1 rounded-full text-[11px] font-semibold">
            Read &amp; Visual (3)
          </button>
          <button onclick="filterStudyModes('labs', this)" class="mode-cat-btn gsap-btn pill-outlined px-3 py-1 rounded-full text-[11px] font-semibold">
            Labs &amp; Stats (3)
          </button>
        </div>

        <!-- Study Modes Grid (Shows 3-4 focused cards per tab instead of 10 at once) -->
        <div id="studyModesGrid" class="px-5 grid grid-cols-2 gap-2.5">
          <!-- Group 1: Active Recall (Default Visible) -->
          <button data-mode-group="recall" class="study-mode-card gsap-btn edu-card p-3 text-left flex flex-col justify-between">
            <div class="w-8 h-8 rounded-xl badge-coral flex items-center justify-center font-bold text-xs">🗂️</div>
            <div class="mt-2">
              <div class="text-[13px] font-extrabold text-[#18152d]">Flashcards</div>
              <div class="text-[10px] text-[#8b87a0]">Review all cards</div>
              <div class="text-[11px] font-bold text-[#e06842] mt-1">110 cards</div>
            </div>
          </button>

          <button data-mode-group="recall" class="study-mode-card gsap-btn edu-card p-3 text-left flex flex-col justify-between">
            <div class="w-8 h-8 rounded-xl badge-lavender flex items-center justify-center font-bold text-xs">☑️</div>
            <div class="mt-2">
              <div class="text-[13px] font-extrabold text-[#18152d]">Multiple Choice</div>
              <div class="text-[10px] text-[#8b87a0]">4-option questions</div>
              <div class="text-[11px] font-bold text-[#5928c9] mt-1">93 questions</div>
            </div>
          </button>

          <button data-mode-group="recall" class="study-mode-card gsap-btn edu-card p-3 text-left flex flex-col justify-between">
            <div class="w-8 h-8 rounded-xl badge-emerald flex items-center justify-center font-bold text-xs">📋</div>
            <div class="mt-2">
              <div class="text-[13px] font-extrabold text-[#18152d]">Enumeration</div>
              <div class="text-[10px] text-[#8b87a0]">Recall the list</div>
              <div class="text-[11px] font-bold text-[#0d9462] mt-1">17 sets</div>
            </div>
          </button>

          <button data-mode-group="recall" disabled class="study-mode-card edu-card p-3 text-left flex flex-col justify-between opacity-50 cursor-not-allowed">
            <div class="w-8 h-8 rounded-xl bg-slate-100 text-slate-500 flex items-center justify-center font-bold text-xs">⚖️</div>
            <div class="mt-2">
              <div class="text-[13px] font-extrabold text-[#18152d]">True / False</div>
              <div class="text-[10px] text-[#8b87a0]">True or false?</div>
              <div class="text-[11px] font-bold text-slate-400 mt-1">0 questions</div>
            </div>
          </button>

          <!-- Group 2: Read & Visual (Hidden until clicked) -->
          <button data-mode-group="content" class="hidden study-mode-card gsap-btn edu-card p-3 text-left flex flex-col justify-between">
            <div class="w-8 h-8 rounded-xl badge-lavender flex items-center justify-center font-bold text-xs">✍️</div>
            <div class="mt-2">
              <div class="text-[13px] font-extrabold text-[#18152d]">Fill in Blanks</div>
              <div class="text-[10px] text-[#8b87a0]">Interactive reading</div>
              <div class="text-[11px] font-bold text-[#5928c9] mt-1">Docs</div>
            </div>
          </button>

          <button data-mode-group="content" class="hidden study-mode-card gsap-btn edu-card p-3 text-left flex flex-col justify-between">
            <div class="w-8 h-8 rounded-xl badge-emerald flex items-center justify-center font-bold text-xs">📖</div>
            <div class="mt-2">
              <div class="text-[13px] font-extrabold text-[#18152d]">Notes</div>
              <div class="text-[10px] text-[#8b87a0]">Key terms &amp; defs</div>
              <div class="text-[11px] font-bold text-[#0d9462] mt-1">45 terms</div>
            </div>
          </button>

          <button data-mode-group="content" class="hidden study-mode-card gsap-btn edu-card p-3 text-left flex flex-col justify-between col-span-2">
            <div class="flex items-center justify-between">
              <div class="w-8 h-8 rounded-xl badge-coral flex items-center justify-center font-bold text-xs">🖼️</div>
              <span class="text-[11px] font-bold text-[#e06842]">95 photos →</span>
            </div>
            <div class="mt-2">
              <div class="text-[13px] font-extrabold text-[#18152d]">Gallery</div>
              <div class="text-[10px] text-[#8b87a0]">Diagrams &amp; visual notes</div>
            </div>
          </button>

          <!-- Group 3: Labs & Stats (Hidden until clicked) -->
          <button data-mode-group="labs" class="hidden study-mode-card gsap-btn edu-card p-3 text-left flex flex-col justify-between col-span-2">
            <div class="flex items-center justify-between">
              <div class="w-8 h-8 rounded-xl badge-lavender flex items-center justify-center font-bold text-xs">📊</div>
              <span class="text-[12px] font-extrabold text-[#5928c9]">23% Mastery →</span>
            </div>
            <div class="mt-2">
              <div class="text-[13px] font-extrabold text-[#18152d]">Stats</div>
              <div class="text-[10px] text-[#8b87a0]">Your progress &amp; retention analytics</div>
            </div>
          </button>

          <button data-mode-group="labs" disabled class="hidden study-mode-card edu-card p-3 text-left flex flex-col justify-between opacity-50 cursor-not-allowed">
            <div class="w-8 h-8 rounded-xl bg-slate-100 flex items-center justify-center text-xs">🧮</div>
            <div class="mt-2">
              <div class="text-[13px] font-extrabold text-[#18152d]">Math Lab</div>
              <div class="text-[10px] text-[#8b87a0]">Step-by-step solver</div>
              <div class="text-[10px] font-bold text-slate-400 mt-1">No math rows</div>
            </div>
          </button>

          <button data-mode-group="labs" disabled class="hidden study-mode-card edu-card p-3 text-left flex flex-col justify-between opacity-50 cursor-not-allowed">
            <div class="w-8 h-8 rounded-xl bg-slate-100 flex items-center justify-center text-xs">💻</div>
            <div class="mt-2">
              <div class="text-[13px] font-extrabold text-[#18152d]">Code Lab</div>
              <div class="text-[10px] text-[#8b87a0]">Interactive runner</div>
              <div class="text-[10px] font-bold text-slate-400 mt-1">No code rows</div>
            </div>
          </button>
        </div>
      </div>

      {bottom_navbar(active_tab="library", is_showcase=is_showcase)}
    </section>
"""

SHARED_SCRIPTS = """
  <script>
    // Progressive Disclosure: My Library Deck Filter & Drawer
    function toggleMoreDecks() {
      const more = document.getElementById('moreDecksContainer');
      const btn = document.getElementById('toggleMoreDecksBtn');
      if (!more || !btn) return;
      const isHidden = more.classList.contains('hidden');
      if (isHidden) {
        more.classList.remove('hidden');
        btn.textContent = 'Show Fewer Decks ↑';
        if (window.gsap) {
          gsap.fromTo(more.children, { opacity: 0, y: 10 }, { opacity: 1, y: 0, duration: 0.28, stagger: 0.06, ease: 'power2.out' });
        }
      } else {
        more.classList.add('hidden');
        btn.textContent = 'Show 2 More Decks (Elementary Sciences & JS) ↓';
      }
    }

    function filterLibraryDecks(cat, clickedBtn) {
      document.querySelectorAll('.lib-filter-btn').forEach(b => {
        b.classList.remove('pill-coral-active');
        b.classList.add('pill-outlined');
      });
      if (clickedBtn) {
        clickedBtn.classList.add('pill-coral-active');
        clickedBtn.classList.remove('pill-outlined');
      }
      const more = document.getElementById('moreDecksContainer');
      const toggleBtn = document.getElementById('toggleMoreDecksBtn');
      if (more) more.classList.remove('hidden');
      if (toggleBtn) toggleBtn.classList.add('hidden');

      document.querySelectorAll('#libraryDecksList .deck-item').forEach(card => {
        const match = (cat === 'all') || (card.getAttribute('data-cat') === cat);
        card.style.display = match ? '' : 'none';
      });
    }

    // Public Feed Search & Folder Filter
    function selectFolderPill(btn) {
      document.querySelectorAll('.folder-pill').forEach(b => {
        b.classList.remove('pill-coral-active');
        b.classList.add('pill-outlined');
      });
      btn.classList.add('pill-coral-active');
      btn.classList.remove('pill-outlined');
    }

    function filterFeedCard(q) {
      const card = document.getElementById('publicDeckCard');
      if (!card) return;
      const text = card.innerText.toLowerCase();
      card.style.display = text.includes((q || '').toLowerCase()) ? '' : 'none';
    }

    // Leaderboard Mode Switcher
    function switchRankTab(label, val, btn) {
      document.querySelectorAll('.rank-mode-btn').forEach(b => {
        b.classList.remove('pill-coral-active');
        b.classList.add('text-white/80');
      });
      btn.classList.add('pill-coral-active');
      btn.classList.remove('text-white/80');
      const lbl = document.getElementById('rankMetricLabel');
      const v = document.getElementById('rankMetricValue');
      const th = document.getElementById('tableMetricHeader');
      const r1 = document.getElementById('row1MetricVal');
      if (lbl) lbl.textContent = label;
      if (v) v.textContent = val;
      if (th) th.textContent = label;
      if (r1) r1.textContent = (label === 'Streak' ? '🔥 ' : '✨ ') + val;
    }

    // Android Progressive Disclosure Tabs
    function switchAndroidTab(tab, btn) {
      document.querySelectorAll('.android-tab-btn').forEach(b => {
        b.classList.remove('pill-coral-active');
        b.classList.add('pill-outlined');
      });
      btn.classList.add('pill-coral-active');
      btn.classList.remove('pill-outlined');
      const qr = document.getElementById('androidTabQR');
      const feat = document.getElementById('androidTabFeatures');
      if (tab === 'qr') {
        if (qr) qr.classList.remove('hidden');
        if (feat) feat.classList.add('hidden');
      } else {
        if (qr) qr.classList.add('hidden');
        if (feat) {
          feat.classList.remove('hidden');
          if (window.gsap) gsap.fromTo(feat.children, { opacity: 0, y: 10 }, { opacity: 1, y: 0, duration: 0.25, stagger: 0.05 });
        }
      }
    }

    // Deck Study Modes Progressive Disclosure Category Filter
    function filterStudyModes(group, btn) {
      document.querySelectorAll('.mode-cat-btn').forEach(b => {
        b.classList.remove('pill-coral-active');
        b.classList.add('pill-outlined');
      });
      btn.classList.add('pill-coral-active');
      btn.classList.remove('pill-outlined');
      document.querySelectorAll('#studyModesGrid .study-mode-card').forEach(card => {
        if (card.getAttribute('data-mode-group') === group) {
          card.classList.remove('hidden');
          if (window.gsap) gsap.fromTo(card, { opacity: 0, y: 8 }, { opacity: 1, y: 0, duration: 0.22 });
        } else {
          card.classList.add('hidden');
        }
      });
    }

    // GSAP Interactive Button & Mascot Animations
    document.addEventListener('DOMContentLoaded', () => {
      if (!window.gsap) return;

      // Subtle floating animation on the single mascot
      const mascot = document.getElementById('mascot-screen1');
      if (mascot) {
        gsap.to(mascot, { y: -4, duration: 2.2, repeat: -1, yoyo: true, ease: 'sine.inOut' });
        mascot.addEventListener('click', () => {
          gsap.timeline()
            .to(mascot, { scaleX: 1.12, scaleY: 0.88, duration: 0.12, ease: 'power2.out' })
            .to(mascot, { scaleX: 0.94, scaleY: 1.08, y: -12, duration: 0.18, ease: 'power2.out' })
            .to(mascot, { scaleX: 1, scaleY: 1, y: 0, duration: 0.45, ease: 'elastic.out(1, 0.4)' });
        });
      }

      // Tactile Squash & Rebound Press on all .gsap-btn elements
      document.querySelectorAll('.gsap-btn').forEach(btn => {
        btn.addEventListener('pointerdown', () => {
          gsap.to(btn, { scaleX: 1.05, scaleY: 0.92, duration: 0.1, ease: 'power2.out' });
        });
        const release = () => {
          gsap.to(btn, { scaleX: 1, scaleY: 1, duration: 0.38, ease: 'elastic.out(1, 0.4)' });
        };
        btn.addEventListener('pointerup', release);
        btn.addEventListener('pointerleave', release);
      });
    });
  </script>
"""

def build_standalone_slide(title, active_slide_num, screen_html):
    head = SHARED_HEAD.replace("__PAGE_TITLE__", title)
    nav_pills = f"""
  <!-- Top Slide Navigation Bar -->
  <div class="my-5 flex flex-wrap items-center justify-center gap-2 bg-white/85 backdrop-blur-md px-4 py-2 rounded-full shadow-sm border border-white text-xs font-semibold text-[#18152d] z-50">
    <a href="educational_app_ui_showcase.html" class="px-3 py-1 rounded-full bg-[#18152d] text-white font-bold">All 5 Screens Showcase</a>
    <a href="slide-StudyUp-2026-11-01T19-33-17.html" class="px-3 py-1 rounded-full {'pill-coral-active' if active_slide_num==1 else 'hover:bg-slate-100'}">1. My Library</a>
    <a href="slide-StudyUp-2026-11-01T19-33-39.html" class="px-3 py-1 rounded-full {'pill-coral-active' if active_slide_num==2 else 'hover:bg-slate-100'}">2. Public Feed</a>
    <a href="slide-StudyUp-2026-11-01T19-33-49.html" class="px-3 py-1 rounded-full {'pill-coral-active' if active_slide_num==3 else 'hover:bg-slate-100'}">3. Leaderboard</a>
    <a href="slide-StudyUp-2026-11-01T19-34-17.html" class="px-3 py-1 rounded-full {'pill-coral-active' if active_slide_num==4 else 'hover:bg-slate-100'}">4. Android App</a>
    <a href="slide-StudyUp-2026-11-01T19-35-38.html" class="px-3 py-1 rounded-full {'pill-coral-active' if active_slide_num==5 else 'hover:bg-slate-100'}">5. Deck Study Modes</a>
  </div>
"""
    return f"""{head}
<body class="py-4 px-4">
  {nav_pills}
  <main class="flex items-center justify-center pb-8">
    {screen_html}
  </main>
  {SHARED_SCRIPTS}
</body>
</html>
"""

def build_showcase_html():
    head = SHARED_HEAD.replace("__PAGE_TITLE__", "StudyUp Educational App UI — Interactive Showcase")
    s1 = build_screen1_inner(is_showcase=True)
    s2 = build_screen2_inner(is_showcase=True)
    s3 = build_screen3_inner(is_showcase=True)
    s4 = build_screen4_inner(is_showcase=True)
    s5 = build_screen5_inner(is_showcase=True)

    return f"""{head}
<body class="py-5 px-4 md:py-8 md:px-6">
  <!-- Top View Mode & Progressive Screen Switcher -->
  <div class="mb-6 flex flex-wrap items-center justify-center gap-2 bg-white/90 backdrop-blur-md px-4 py-2.5 rounded-full shadow-sm border border-white text-xs font-semibold text-[#18152d] z-50">
    <span class="text-[#8b87a0] font-bold uppercase tracking-wider text-[10px] pl-1">Mode:</span>
    <button id="btnSingleView" onclick="setShowcaseMode('single')" class="gsap-btn px-3.5 py-1.5 rounded-full bg-[#18152d] text-white font-bold shadow-sm">
      Focused Single Phone (Recommended)
    </button>
    <button id="btnGridView" onclick="setShowcaseMode('grid')" class="gsap-btn px-3.5 py-1.5 rounded-full hover:bg-slate-100 text-[#2c2647] font-semibold">
      Compare All 5 Screens
    </button>

    <div class="flex items-center gap-1 pl-2 border-l border-slate-200 flex-wrap justify-center">
      <button onclick="switchPhoneScreen(1)" id="topTab1" class="screen-pill gsap-btn pill-coral-active px-3 py-1 rounded-full text-[11px] font-bold">1. My Library</button>
      <button onclick="switchPhoneScreen(2)" id="topTab2" class="screen-pill gsap-btn pill-outlined px-3 py-1 rounded-full text-[11px] font-semibold">2. Public Feed</button>
      <button onclick="switchPhoneScreen(3)" id="topTab3" class="screen-pill gsap-btn pill-outlined px-3 py-1 rounded-full text-[11px] font-semibold">3. Leaderboard</button>
      <button onclick="switchPhoneScreen(4)" id="topTab4" class="screen-pill gsap-btn pill-outlined px-3 py-1 rounded-full text-[11px] font-semibold">4. Android App</button>
      <button onclick="switchPhoneScreen(5)" id="topTab5" class="screen-pill gsap-btn pill-outlined px-3 py-1 rounded-full text-[11px] font-semibold">5. Study Modes</button>
    </div>
  </div>

  <!-- Main Screens Container (Defaults to Focused Single-Phone Progressive Disclosure View) -->
  <main id="screensContainer" class="flex flex-wrap items-center justify-center gap-8 max-w-[1480px] mx-auto pb-8">
    <div id="wrapScreen1" class="phone-wrapper">{s1}</div>
    <div id="wrapScreen2" class="phone-wrapper hidden">{s2}</div>
    <div id="wrapScreen3" class="phone-wrapper hidden">{s3}</div>
    <div id="wrapScreen4" class="phone-wrapper hidden">{s4}</div>
    <div id="wrapScreen5" class="phone-wrapper hidden">{s5}</div>
  </main>

  {SHARED_SCRIPTS}
  <script>
    let currentShowcaseMode = 'single';
    let activeScreenNum = 1;

    function setShowcaseMode(mode) {
      currentShowcaseMode = mode;
      const btnSingle = document.getElementById('btnSingleView');
      const btnGrid = document.getElementById('btnGridView');
      const wrappers = document.querySelectorAll('.phone-wrapper');

      if (mode === 'single') {
        btnSingle.className = 'gsap-btn px-3.5 py-1.5 rounded-full bg-[#18152d] text-white font-bold shadow-sm';
        btnGrid.className = 'gsap-btn px-3.5 py-1.5 rounded-full hover:bg-slate-100 text-[#2c2647] font-semibold';
        wrappers.forEach((w, idx) => {
          w.classList.toggle('hidden', (idx + 1) !== activeScreenNum);
        });
      } else {
        btnGrid.className = 'gsap-btn px-3.5 py-1.5 rounded-full bg-[#18152d] text-white font-bold shadow-sm';
        btnSingle.className = 'gsap-btn px-3.5 py-1.5 rounded-full hover:bg-slate-100 text-[#2c2647] font-semibold';
        wrappers.forEach(w => w.classList.remove('hidden'));
        if (window.gsap) {
          gsap.fromTo('.phone-wrapper', { opacity: 0, y: 16 }, { opacity: 1, y: 0, duration: 0.35, stagger: 0.06, ease: 'power2.out' });
        }
      }
    }

    function switchPhoneScreen(num) {
      activeScreenNum = num;
      for (let i = 1; i <= 5; i++) {
        const tab = document.getElementById('topTab' + i);
        if (tab) {
          if (i === num) {
            tab.classList.add('pill-coral-active');
            tab.classList.remove('pill-outlined');
          } else {
            tab.classList.remove('pill-coral-active');
            tab.classList.add('pill-outlined');
          }
        }
      }

      if (currentShowcaseMode === 'single') {
        for (let i = 1; i <= 5; i++) {
          const w = document.getElementById('wrapScreen' + i);
          if (w) {
            if (i === num) {
              w.classList.remove('hidden');
              if (window.gsap) gsap.fromTo(w, { opacity: 0, x: 18 }, { opacity: 1, x: 0, duration: 0.28, ease: 'power2.out' });
            } else {
              w.classList.add('hidden');
            }
          }
        }
      } else {
        const target = document.getElementById('screen' + num);
        document.querySelectorAll('.phone-frame').forEach(f => f.classList.remove('highlight-ring'));
        if (target) {
          target.classList.add('highlight-ring');
          target.scrollIntoView({ behavior: 'smooth', block: 'center', inline: 'center' });
        }
      }
    }
  </script>
</body>
</html>
"""

slides = {
    "slide-StudyUp-2026-11-01T19-33-17.html": build_standalone_slide("StudyUp — My Library", 1, build_screen1_inner(is_showcase=False)),
    "slide-StudyUp-2026-11-01T19-33-39.html": build_standalone_slide("StudyUp — Public Feed", 2, build_screen2_inner(is_showcase=False)),
    "slide-StudyUp-2026-11-01T19-33-49.html": build_standalone_slide("StudyUp — Leaderboard", 3, build_screen3_inner(is_showcase=False)),
    "slide-StudyUp-2026-11-01T19-34-17.html": build_standalone_slide("StudyUp — Android App", 4, build_screen4_inner(is_showcase=False)),
    "slide-StudyUp-2026-11-01T19-35-38.html": build_standalone_slide("StudyUp — Deck Study Modes", 5, build_screen5_inner(is_showcase=False)),
    "educational_app_ui_showcase.html": build_showcase_html(),
}

for fname, content in slides.items():
    root_path = os.path.join(ROOT_DIR, fname)
    dl_path = os.path.join(DOWNLOADS_DIR, fname)
    with open(root_path, "w", encoding="utf-8") as f:
        f.write(content)
    with open(dl_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Wrote {fname} ({len(content):,} bytes) to Root & Downloads")

# Also sync index.html to point to educational_app_ui_showcase.html and all 5 StudyUp slides
shutil.copyfile(os.path.join(ROOT_DIR, "educational_app_ui_showcase.html"), os.path.join(ROOT_DIR, "index.html"))
print("Synced index.html")
