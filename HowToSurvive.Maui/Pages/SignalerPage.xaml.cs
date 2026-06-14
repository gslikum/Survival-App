using System;
using System.Threading;
using System.Threading.Tasks;
using Microsoft.Maui.ApplicationModel;
using Microsoft.Maui.Controls;
using Microsoft.Maui.Graphics;

namespace HowToSurvive.Maui.Pages
{
    public partial class SignalerPage : ContentPage
    {
        private bool _isFlashing = false;
        private CancellationTokenSource? _cts;

        public SignalerPage()
        {
            InitializeComponent();
        }

        protected override void OnDisappearing()
        {
            base.OnDisappearing();
            StopFlashing();
        }

        private void OnToggleFlashClicked(object sender, EventArgs e)
        {
            if (_isFlashing)
            {
                StopFlashing();
            }
            else
            {
                StartFlashing();
            }
        }

        private void StartFlashing()
        {
            _isFlashing = true;
            ToggleFlashBtn.Text = "STOP SOS TRANSMISSION";
            ToggleFlashBtn.BackgroundColor = Colors.Red;
            _cts = new CancellationTokenSource();
            
            var token = _cts.Token;
            Task.Run(async () => await FlashingLoop(token), token);
        }

        private void StopFlashing()
        {
            _isFlashing = false;
            _cts?.Cancel();
            _cts = null;
            
            ToggleFlashBtn.Text = "START SOS TRANSMISSION";
            ToggleFlashBtn.BackgroundColor = (Color)Application.Current!.Resources["Secondary"];
            FlashIndicatorFrame.BackgroundColor = (Color)Application.Current!.Resources["Gray950"];
            FlashStatusLabel.Text = "SIGNAL INACTIVE";
            FlashStatusLabel.TextColor = (Color)Application.Current!.Resources["Gray500"];
        }

        private async Task FlashingLoop(CancellationToken token)
        {
            int dot = 250;
            int dash = 750;
            int elementGap = 250;
            int letterGap = 750;
            int wordGap = 1750;

            try
            {
                while (!token.IsCancellationRequested)
                {
                    // S (...)
                    await Flash(dot, "S  [ . ]", token);
                    await Task.Delay(elementGap, token);
                    await Flash(dot, "S  [ . ]", token);
                    await Task.Delay(elementGap, token);
                    await Flash(dot, "S  [ . ]", token);
                    
                    await Task.Delay(letterGap, token);

                    // O (---)
                    await Flash(dash, "O  [ - ]", token);
                    await Task.Delay(elementGap, token);
                    await Flash(dash, "O  [ - ]", token);
                    await Task.Delay(elementGap, token);
                    await Flash(dash, "O  [ - ]", token);

                    await Task.Delay(letterGap, token);

                    // S (...)
                    await Flash(dot, "S  [ . ]", token);
                    await Task.Delay(elementGap, token);
                    await Flash(dot, "S  [ . ]", token);
                    await Task.Delay(elementGap, token);
                    await Flash(dot, "S  [ . ]", token);

                    // Word Gap
                    MainThread.BeginInvokeOnMainThread(() =>
                    {
                        FlashIndicatorFrame.BackgroundColor = (Color)Application.Current!.Resources["Gray950"];
                        FlashStatusLabel.Text = "GAP";
                        FlashStatusLabel.TextColor = (Color)Application.Current!.Resources["Gray500"];
                    });
                    await Task.Delay(wordGap, token);
                }
            }
            catch (TaskCanceledException)
            {
                // Exit cleanly
            }
            catch (Exception)
            {
                // Handle or ignore
            }
        }

        private async Task Flash(int durationMs, string statusText, CancellationToken token)
        {
            MainThread.BeginInvokeOnMainThread(() =>
            {
                FlashIndicatorFrame.BackgroundColor = Colors.White;
                FlashStatusLabel.Text = statusText;
                FlashStatusLabel.TextColor = Colors.Black;
            });

            await Task.Delay(durationMs, token);

            MainThread.BeginInvokeOnMainThread(() =>
            {
                FlashIndicatorFrame.BackgroundColor = (Color)Application.Current!.Resources["Gray950"];
                FlashStatusLabel.Text = "";
                FlashStatusLabel.TextColor = (Color)Application.Current!.Resources["Gray500"];
            });
        }
    }
}
