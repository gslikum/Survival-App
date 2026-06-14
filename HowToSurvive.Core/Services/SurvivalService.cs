using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Text.Json;
using HowToSurvive.Core.Models;

namespace HowToSurvive.Core.Services
{
    public class SurvivalService
    {
        private List<SurvivalChapter> _chapters = new();
        private bool _isLoaded;

        public SurvivalService()
        {
            LoadBookContent();
        }

        private void LoadBookContent()
        {
            if (_isLoaded) return;
            try
            {
                var assembly = Assembly.GetExecutingAssembly();
                // Find resource name
                var resourceName = assembly.GetManifestResourceNames()
                    .FirstOrDefault(r => r.EndsWith("survival_content.json"));

                if (string.IsNullOrEmpty(resourceName))
                {
                    Console.WriteLine("Warning: survival_content.json resource not found.");
                    return;
                }

                using (Stream? stream = assembly.GetManifestResourceStream(resourceName))
                {
                    if (stream == null) return;
                    using (StreamReader reader = new StreamReader(stream))
                    {
                        string json = reader.ReadToEnd();
                        var options = new JsonSerializerOptions
                        {
                            PropertyNameCaseInsensitive = true
                        };
                        var parsed = JsonSerializer.Deserialize<List<SurvivalChapter>>(json, options);
                        if (parsed != null)
                        {
                            _chapters = parsed;
                            _isLoaded = true;
                        }
                    }
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error loading survival content: {ex.Message}");
            }
        }

        public List<SurvivalChapter> GetChapters()
        {
            LoadBookContent();
            return _chapters;
        }

        public SurvivalChapter? GetChapter(string title)
        {
            LoadBookContent();
            return _chapters.FirstOrDefault(c => c.Title.Equals(title, StringComparison.OrdinalIgnoreCase));
        }

        public SurvivalArticle? GetArticle(string chapterTitle, string articleTitle)
        {
            var chapter = GetChapter(chapterTitle);
            return chapter?.Articles.FirstOrDefault(a => a.Title.Equals(articleTitle, StringComparison.OrdinalIgnoreCase));
        }

        public List<(SurvivalChapter Chapter, SurvivalArticle Article)> SearchArticles(string query)
        {
            LoadBookContent();
            var results = new List<(SurvivalChapter Chapter, SurvivalArticle Article)>();
            if (string.IsNullOrWhiteSpace(query)) return results;

            var q = query.ToLowerInvariant();
            foreach (var chapter in _chapters)
            {
                foreach (var article in chapter.Articles)
                {
                    bool matchTitle = article.Title.ToLowerInvariant().Contains(q) || 
                                     article.Subtitle.ToLowerInvariant().Contains(q);
                    
                    bool matchContent = article.TextSections.Any(s => s.ToLowerInvariant().Contains(q));

                    if (matchTitle || matchContent)
                    {
                        results.Add((chapter, article));
                    }
                }
            }
            return results;
        }

        public List<ChecklistItem> GetDefaultChecklistItems()
        {
            return new List<ChecklistItem>
            {
                // Bug-Out Bag
                new() { Id = "bob_1", Name = "Water filter or purification tablets", Category = "Bug-Out Bag", IsCompleted = false },
                new() { Id = "bob_2", Name = "Tactical knife / Multi-tool", Category = "Bug-Out Bag", IsCompleted = false },
                new() { Id = "bob_3", Name = "Tarp or lightweight shelter", Category = "Bug-Out Bag", IsCompleted = false },
                new() { Id = "bob_4", Name = "Fire starter (Ferro rod / Matches)", Category = "Bug-Out Bag", IsCompleted = false },
                new() { Id = "bob_5", Name = "High-calorie rations (72 hours)", Category = "Bug-Out Bag", IsCompleted = false },
                new() { Id = "bob_6", Name = "First aid kit", Category = "Bug-Out Bag", IsCompleted = false },
                new() { Id = "bob_7", Name = "Flashlight with extra batteries", Category = "Bug-Out Bag", IsCompleted = false },
                new() { Id = "bob_8", Name = "50 feet of 550 Paracord", Category = "Bug-Out Bag", IsCompleted = false },

                // Survival Tin
                new() { Id = "tin_1", Name = "Matches (Waterproofed in paraffin wax)", Category = "Survival Tin", IsCompleted = false },
                new() { Id = "tin_2", Name = "Candle (Shaved down to fit)", Category = "Survival Tin", IsCompleted = false },
                new() { Id = "tin_3", Name = "Flint & Striker (Ferrocerium rod)", Category = "Survival Tin", IsCompleted = false },
                new() { Id = "tin_4", Name = "Button Compass (Liquid-filled)", Category = "Survival Tin", IsCompleted = false },
                new() { Id = "tin_5", Name = "Snare Wire (Brass wire, 60-90 cm)", Category = "Survival Tin", IsCompleted = false },
                new() { Id = "tin_6", Name = "Sewing Kit (Heavy needles & thread)", Category = "Survival Tin", IsCompleted = false },
                new() { Id = "tin_7", Name = "Fishing Tackle (Line, hooks, sinkers, swivels)", Category = "Survival Tin", IsCompleted = false },
                new() { Id = "tin_8", Name = "Wire Saw (Flexible, with finger rings)", Category = "Survival Tin", IsCompleted = false },
                new() { Id = "tin_9", Name = "Scalpel Blades (Two different sizes)", Category = "Survival Tin", IsCompleted = false },
                new() { Id = "tin_10", Name = "Adhesive Plasters (Waterproof dressings)", Category = "Survival Tin", IsCompleted = false },
                new() { Id = "tin_11", Name = "Water Sterilizer (Chlorine/iodine tablets)", Category = "Survival Tin", IsCompleted = false },
                new() { Id = "tin_12", Name = "Condom (1 liter water container)", Category = "Survival Tin", IsCompleted = false },

                // Camp Setup
                new() { Id = "camp_1", Name = "Locate flat, dry ground away from dead trees", Category = "Camp Setup", IsCompleted = false },
                new() { Id = "camp_2", Name = "Build Lean-To or Debris Hut shelter", Category = "Camp Setup", IsCompleted = false },
                new() { Id = "camp_3", Name = "Create a 6-inch insulating mattress of leaves", Category = "Camp Setup", IsCompleted = false },
                new() { Id = "camp_4", Name = "Collect wood: Tinder, Kindling, and Fuel stacks", Category = "Camp Setup", IsCompleted = false },
                new() { Id = "camp_5", Name = "Establish clean water source (boil or filter)", Category = "Camp Setup", IsCompleted = false },
                new() { Id = "camp_6", Name = "Prepare rescue signals (fires / mirror / ground sign)", Category = "Camp Setup", IsCompleted = false }
            };
        }

        public List<FlowchartNode> GetFirstAidFlowchart()
        {
            return new List<FlowchartNode>
            {
                new() {
                    Id = "root",
                    QuestionText = "Is the victim responsive and conscious?",
                    YesNodeId = "conscious_flow",
                    NoNodeId = "unconscious_flow"
                },
                new() {
                    Id = "conscious_flow",
                    QuestionText = "Is the victim bleeding severely?",
                    YesNodeId = "severe_bleeding",
                    NoNodeId = "conscious_other"
                },
                new() {
                    Id = "unconscious_flow",
                    QuestionText = "Is the victim breathing normally?",
                    YesNodeId = "recovery_position",
                    NoNodeId = "cpr_start"
                },
                new() {
                    Id = "severe_bleeding",
                    AdviceText = "Apply direct, firm pressure to the wound with a clean cloth. Elevate the injured limb above the heart. If bleeding is life-threatening and cannot be stopped by pressure, apply a tourniquet 2 inches above the wound on a single bone (upper arm or thigh). Keep the victim warm and treat for shock."
                },
                new() {
                    Id = "conscious_other",
                    AdviceText = "Perform secondary checks. For fractures, immobilize the limb with splints. For snake bites, keep the limb still, wrap it firmly, and keep it below heart level. Treat heat exhaustion with shade and sips of water. Monitor breathing constantly."
                },
                new() {
                    Id = "recovery_position",
                    AdviceText = "Place the victim in the Recovery Position. Roll them onto their side, tilt their head back to keep the airway clear, and bend their top knee at a right angle to prevent them from rolling onto their stomach. Monitor their breathing continually."
                },
                new() {
                    Id = "cpr_start",
                    AdviceText = "Begin Cardiopulmonary Resuscitation (CPR) immediately. Place your hands in the center of the chest, lock your elbows, and perform 30 chest compressions at 100-120 per minute (2 inches deep), followed by 2 rescue breaths. If untrained or unable, perform continuous chest compressions."
                }
            };
        }
    }
}
