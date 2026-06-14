using System.Collections.Generic;

namespace HowToSurvive.Core.Models
{
    public class SurvivalChapter
    {
        public string Title { get; set; } = string.Empty;
        public string Description { get; set; } = string.Empty;
        public List<SurvivalArticle> Articles { get; set; } = new();
    }

    public class SurvivalArticle
    {
        public string Title { get; set; } = string.Empty;
        public string Subtitle { get; set; } = string.Empty;
        public string ImageName { get; set; } = string.Empty;
        public List<string> TextSections { get; set; } = new();
        public List<SurvivalItem> Items { get; set; } = new();
    }

    public class SurvivalItem
    {
        public string Name { get; set; } = string.Empty;
        public string Description { get; set; } = string.Empty;
        public string ImageName { get; set; } = string.Empty;
    }

    public class ChecklistItem
    {
        public string Id { get; set; } = string.Empty;
        public string Name { get; set; } = string.Empty;
        public string Category { get; set; } = string.Empty;
        public bool IsCompleted { get; set; }
    }

    public class FlowchartNode
    {
        public string Id { get; set; } = string.Empty;
        public string QuestionText { get; set; } = string.Empty;
        public string YesNodeId { get; set; } = string.Empty;
        public string NoNodeId { get; set; } = string.Empty;
        public string AdviceText { get; set; } = string.Empty;
        public bool IsDecision => !string.IsNullOrEmpty(QuestionText);
    }
}
