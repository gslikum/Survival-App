using System;
using System.Linq;
using Microsoft.Maui.Controls;
using HowToSurvive.Core.Services;

namespace HowToSurvive.Maui
{
    public partial class MainPage : ContentPage
    {
        private readonly SurvivalService _survivalService;

        public MainPage(SurvivalService survivalService)
        {
            InitializeComponent();
            _survivalService = survivalService;
        }

        private async void OnChapterTapped(object sender, TappedEventArgs e)
        {
            if (e.Parameter is string chapterTitle)
            {
                await Shell.Current.GoToAsync($"chapterPage?chapterTitle={Uri.EscapeDataString(chapterTitle)}");
            }
        }

        private void OnSearchTextChanged(object sender, TextChangedEventArgs e)
        {
            string text = e.NewTextValue?.Trim() ?? string.Empty;
            if (string.IsNullOrWhiteSpace(text))
            {
                SearchResultsStack.IsVisible = false;
                ChaptersLayout.IsVisible = true;
                ClearSearchBtn.IsVisible = false;
            }
            else
            {
                var results = _survivalService.SearchArticles(text);
                SearchResultsCollectionView.ItemsSource = results;
                SearchResultsStack.IsVisible = true;
                ChaptersLayout.IsVisible = false;
                ClearSearchBtn.IsVisible = true;
            }
        }

        private void OnClearSearchClicked(object sender, EventArgs e)
        {
            SearchEntry.Text = string.Empty;
        }

        private async void OnSearchResultSelected(object sender, SelectionChangedEventArgs e)
        {
            var selectedItem = e.CurrentSelection.FirstOrDefault();
            if (selectedItem is ValueTuple<Core.Models.SurvivalChapter, Core.Models.SurvivalArticle> selection)
            {
                SearchResultsCollectionView.SelectedItem = null;
                await Shell.Current.GoToAsync($"articlePage?chapterTitle={Uri.EscapeDataString(selection.Item1.Title)}&articleTitle={Uri.EscapeDataString(selection.Item2.Title)}");
            }
        }

        private async void OnEmergencyClicked(object sender, EventArgs e)
        {
            await Shell.Current.GoToAsync("//firstAid");
        }

        private async void OnSignalerClicked(object sender, EventArgs e)
        {
            await Shell.Current.GoToAsync("//signaler");
        }
    }
}
