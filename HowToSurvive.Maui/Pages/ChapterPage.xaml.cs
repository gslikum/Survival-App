using System;
using System.Linq;
using Microsoft.Maui.Controls;
using HowToSurvive.Core.Models;
using HowToSurvive.Core.Services;

namespace HowToSurvive.Maui.Pages
{
    [QueryProperty(nameof(ChapterTitle), "chapterTitle")]
    public partial class ChapterPage : ContentPage
    {
        private readonly SurvivalService _survivalService;
        private string _chapterTitle = string.Empty;

        public string ChapterTitle
        {
            get => _chapterTitle;
            set
            {
                _chapterTitle = Uri.UnescapeDataString(value ?? string.Empty);
                OnPropertyChanged();
                LoadChapterData();
            }
        }

        public ChapterPage(SurvivalService survivalService)
        {
            InitializeComponent();
            _survivalService = survivalService;
            BindingContext = this;
        }

        private void LoadChapterData()
        {
            var chapter = _survivalService.GetChapter(ChapterTitle);
            if (chapter != null)
            {
                ChapterTitleLabel.Text = chapter.Title.ToUpperInvariant();
                ChapterDescriptionLabel.Text = chapter.Description;
                ArticlesCollectionView.ItemsSource = chapter.Articles;
            }
        }

        private async void OnArticleSelected(object sender, SelectionChangedEventArgs e)
        {
            if (e.CurrentSelection.FirstOrDefault() is SurvivalArticle article)
            {
                ArticlesCollectionView.SelectedItem = null;
                // Navigate to ArticlePage
                await Shell.Current.GoToAsync($"articlePage?chapterTitle={Uri.EscapeDataString(ChapterTitle)}&articleTitle={Uri.EscapeDataString(article.Title)}");
            }
        }
    }
}
