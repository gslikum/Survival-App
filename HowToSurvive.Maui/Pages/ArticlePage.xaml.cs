using System;
using Microsoft.Maui;
using Microsoft.Maui.Controls;
using HowToSurvive.Core.Services;

namespace HowToSurvive.Maui.Pages
{
    [QueryProperty(nameof(ChapterTitle), "chapterTitle")]
    [QueryProperty(nameof(ArticleTitle), "articleTitle")]
    public partial class ArticlePage : ContentPage
    {
        private readonly SurvivalService _survivalService;
        private string _chapterTitle = string.Empty;
        private string _articleTitle = string.Empty;

        public string ChapterTitle
        {
            get => _chapterTitle;
            set
            {
                _chapterTitle = Uri.UnescapeDataString(value ?? string.Empty);
                OnPropertyChanged();
                LoadArticleData();
            }
        }

        public string ArticleTitle
        {
            get => _articleTitle;
            set
            {
                _articleTitle = Uri.UnescapeDataString(value ?? string.Empty);
                OnPropertyChanged();
                LoadArticleData();
            }
        }

        public ArticlePage(SurvivalService survivalService)
        {
            InitializeComponent();
            _survivalService = survivalService;
        }

        private void LoadArticleData()
        {
            if (string.IsNullOrEmpty(ChapterTitle) || string.IsNullOrEmpty(ArticleTitle)) return;

            var article = _survivalService.GetArticle(ChapterTitle, ArticleTitle);
            if (article != null)
            {
                ArticleTitleLabel.Text = article.Title;
                ArticleSubtitleLabel.Text = article.Subtitle;
                ArticleImage.Source = article.ImageName;

                // Clear old text sections
                TextSectionsStack.Children.Clear();

                // Populate text sections
                foreach (var paragraph in article.TextSections)
                {
                    var label = new Label
                    {
                        Text = paragraph,
                        FontSize = 16,
                        TextColor = (Color)Application.Current!.Resources["White"],
                        LineHeight = 1.4,
                        Margin = new Thickness(0, 0, 0, 8)
                    };
                    TextSectionsStack.Children.Add(label);
                }

                // Populate sub-items visual inventory if available
                if (article.Items != null && article.Items.Count > 0)
                {
                    var headerLabel = new Label
                    {
                        Text = "Visual Inventory & Specifications",
                        FontSize = 20,
                        FontAttributes = FontAttributes.Bold,
                        TextColor = (Color)Application.Current!.Resources["White"],
                        Margin = new Thickness(0, 20, 0, 12)
                    };
                    TextSectionsStack.Children.Add(headerLabel);

                    foreach (var item in article.Items)
                    {
                        var itemFrame = new Frame
                        {
                            BackgroundColor = Color.FromArgb("#121c17"),
                            BorderColor = Color.FromArgb("#23352c"),
                            CornerRadius = 8,
                            Padding = 10,
                            Margin = new Thickness(0, 0, 0, 10),
                            HasShadow = false
                        };

                        var grid = new Grid
                        {
                            ColumnDefinitions = new ColumnDefinitionCollection
                            {
                                new ColumnDefinition { Width = new GridLength(80) },
                                new ColumnDefinition { Width = GridLength.Star }
                            },
                            ColumnSpacing = 12
                        };

                        var imgFrame = new Frame
                        {
                            Padding = 0,
                            CornerRadius = 6,
                            IsClippedToBounds = true,
                            HeightRequest = 80,
                            WidthRequest = 80,
                            BorderColor = Colors.Transparent,
                            BackgroundColor = Colors.Transparent
                        };

                        var img = new Image
                        {
                            Source = item.ImageName,
                            Aspect = Aspect.AspectFill,
                            WidthRequest = 80,
                            HeightRequest = 80
                        };
                        imgFrame.Content = img;

                        var infoStack = new VerticalStackLayout
                        {
                            Spacing = 4,
                            VerticalOptions = LayoutOptions.Center
                        };

                        var nameLabel = new Label
                        {
                            Text = item.Name,
                            FontSize = 15,
                            FontAttributes = FontAttributes.Bold,
                            TextColor = Color.FromArgb("#ff9f0a")
                        };

                        var descLabel = new Label
                        {
                            Text = item.Description,
                            FontSize = 13,
                            TextColor = Color.FromArgb("#a2b0a6"),
                            LineBreakMode = LineBreakMode.WordWrap
                        };

                        infoStack.Children.Add(nameLabel);
                        infoStack.Children.Add(descLabel);

                        grid.Children.Add(imgFrame);
                        Grid.SetColumn(imgFrame, 0);

                        grid.Children.Add(infoStack);
                        Grid.SetColumn(infoStack, 1);

                        itemFrame.Content = grid;
                        TextSectionsStack.Children.Add(itemFrame);
                    }
                }
            }
        }
    }
}
