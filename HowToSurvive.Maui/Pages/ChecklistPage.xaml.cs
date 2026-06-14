using System;
using System.Collections.Generic;
using System.Linq;
using Microsoft.Maui.Controls;
using Microsoft.Maui.Storage;
using HowToSurvive.Core.Models;
using HowToSurvive.Core.Services;

namespace HowToSurvive.Maui.Pages
{
    public partial class ChecklistPage : ContentPage
    {
        private readonly SurvivalService _survivalService;
        private List<ChecklistItem> _allItems = new();
        private string _currentCategory = "Bug-Out Bag";

        public ChecklistPage(SurvivalService survivalService)
        {
            InitializeComponent();
            _survivalService = survivalService;
        }

        protected override void OnAppearing()
        {
            base.OnAppearing();
            LoadChecklist();
        }

        private void LoadChecklist()
        {
            _allItems = _survivalService.GetDefaultChecklistItems();
            
            // Restore state
            foreach (var item in _allItems)
            {
                item.IsCompleted = Preferences.Default.Get($"chk_{item.Id}", false);
            }

            FilterList();
        }

        private void FilterList()
        {
            var filtered = _allItems.Where(i => i.Category == _currentCategory).ToList();
            ChecklistCollectionView.ItemsSource = filtered;
        }

        private void OnItemCheckChanged(object sender, CheckedChangedEventArgs e)
        {
            if (sender is CheckBox checkBox && checkBox.BindingContext is ChecklistItem item)
            {
                item.IsCompleted = e.Value;
                Preferences.Default.Set($"chk_{item.Id}", e.Value);
            }
        }

        private void OnBobTabClicked(object sender, EventArgs e)
        {
            SetTab("Bug-Out Bag", BobTabBtn, new[] { TinTabBtn, CampTabBtn });
        }

        private void OnTinTabClicked(object sender, EventArgs e)
        {
            SetTab("Survival Tin", TinTabBtn, new[] { BobTabBtn, CampTabBtn });
        }

        private void OnCampTabClicked(object sender, EventArgs e)
        {
            SetTab("Camp Setup", CampTabBtn, new[] { BobTabBtn, TinTabBtn });
        }

        private void SetTab(string category, Button activeBtn, Button[] inactiveBtns)
        {
            _currentCategory = category;
            
            activeBtn.BackgroundColor = (Color)Application.Current!.Resources["Primary"];
            activeBtn.TextColor = Colors.White;

            foreach (var btn in inactiveBtns)
            {
                btn.BackgroundColor = (Color)Application.Current!.Resources["Gray900"];
                btn.TextColor = (Color)Application.Current!.Resources["Gray300"];
            }

            FilterList();
        }
    }
}
