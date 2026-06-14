using Microsoft.Extensions.Logging;

namespace HowToSurvive.Maui;

public static class MauiProgram
{
	public static MauiApp CreateMauiApp()
	{
		var builder = MauiApp.CreateBuilder();
		builder
			.UseMauiApp<App>()
			.ConfigureFonts(fonts =>
			{
				fonts.AddFont("OpenSans-Regular.ttf", "OpenSansRegular");
				fonts.AddFont("OpenSans-Semibold.ttf", "OpenSansSemibold");
			});

		// Register Services
		builder.Services.AddSingleton<HowToSurvive.Core.Services.SurvivalService>();

		// Register Pages
		builder.Services.AddTransient<MainPage>();
		builder.Services.AddTransient<Pages.ChapterPage>();
		builder.Services.AddTransient<Pages.ArticlePage>();
		builder.Services.AddSingleton<Pages.FirstAidPage>();
		builder.Services.AddSingleton<Pages.ChecklistPage>();
		builder.Services.AddSingleton<Pages.SignalerPage>();

#if DEBUG
		builder.Logging.AddDebug();
#endif

		return builder.Build();
	}
}
