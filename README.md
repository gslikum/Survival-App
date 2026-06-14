# SAS Survival Companion

A premium, cross-platform hybrid mobile and web companion application based on John 'Lofty' Wiseman's *SAS Survival Handbook*. Built using **.NET 10**, this solution shares a core database and business logic assembly across a native **.NET MAUI (XAML)** app targeting iOS/macOS and a client-side **Blazor WebAssembly** dashboard.

All components, search indexing, interactive flowcharts, checklists, and imagery function **100% offline**, offering maximum off-grid utility.

---

## Key Features

1. **Structured Survival Handbook**
   * Programmatically parsed and cleaned chapters matching the revised handbook.
   * Dedicated detailed modules for **Essentials** (preparation, climate gear, off-grid communication, GPS, vehicle crash procedures) and **Sourcing Water & Facing Disaster** (fear management, rule of 3s, solar stills, condensation collection, water trees, and salt extraction).
2. **Visual Inventory & Specifications**
   * Dynamic item grids for the **Survival Tin** (12 essential components, from waterproof matches to condom water bags) and **Survival Pouch** (heliographs, signaling mirrors, etc.), complete with photographs.
3. **Emergency Utilities**
   * **Preparedness Checklists**: Locally persistent checklists (Bug-Out Bag, Survival Tin, Camp Setup) working 100% offline via browser storage or device preferences.
   * **Rescue Signaler**: Morse code SOS visual flasher panel blinking in the standard dot-dash pattern (`... --- ...`) along with an international ground-to-air code chart.
   * **Interactive First Aid**: Wizard-based flowchart diagnosing emergencies (CPR, snake bites, severe bleeding) using binary states.
4. **Instant Offline Search**
   * Full-text search querying the entire database offline on the home dashboard.

---

## Architectural Layout

The solution is divided into three logical projects:

* **[HowToSurvive.Core](./HowToSurvive.Core)**: Shared C# library containing model schemas, default checklist definitions, the state-machine first-aid flowchart, and the JSON book database resource (`survival_content.json`).
* **[HowToSurvive.Web](./HowToSurvive.Web)**: Responsive Blazor WebAssembly application built with vanilla CSS.
* **[HowToSurvive.Maui](./HowToSurvive.Maui)**: Native application targeting **iOS** and **macOS (Mac Catalyst)** compiled to native platform controls (no web-view wrapper).

---

## Getting Started

### Prerequisites

* [.NET 10 SDK](https://dotnet.microsoft.com/download)
* Python 3 (for compiling the database json / downloading images)

### Running the Web Application (Blazor)

1. Navigate to the root directory.
2. Run the application:
   ```bash
   dotnet run --project HowToSurvive.Web/HowToSurvive.Web.csproj
   ```
3. Open the localhost port (typically `http://localhost:5071`) in your web browser.

### Running the Native macOS Application (Mac Catalyst)

Run the following command from the workspace root:
```bash
dotnet build -t:Run -f net10.0-maccatalyst HowToSurvive.Maui/HowToSurvive.Maui.csproj
```

### Running/Testing iOS Simulator

```bash
dotnet build -f net10.0-ios HowToSurvive.Maui/HowToSurvive.Maui.csproj
```

---

## Sourcing Images & Data Compilation

The database and assets are programmatically compiled from source. To update them:

1. **Rebuild JSON database**:
   ```bash
   python3 generate_clean_json.py
   ```
2. **Re-download Unsplash items & assets**:
   ```bash
   python3 download_images.py
   ```

---

## License

This project is for educational and portfolio demonstration purposes. All content rights belong to their respective publishers.
