namespace HowToSurvive.Maui;

public partial class AppShell : Shell
{
	public AppShell()
	{
		InitializeComponent();
		Routing.RegisterRoute("chapterPage", typeof(Pages.ChapterPage));
		Routing.RegisterRoute("articlePage", typeof(Pages.ArticlePage));
	}
}
