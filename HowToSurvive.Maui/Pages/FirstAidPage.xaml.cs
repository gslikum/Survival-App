using System;
using System.Collections.Generic;
using System.Linq;
using Microsoft.Maui.Controls;
using HowToSurvive.Core.Models;
using HowToSurvive.Core.Services;

namespace HowToSurvive.Maui.Pages
{
    public partial class FirstAidPage : ContentPage
    {
        private readonly SurvivalService _survivalService;
        private List<FlowchartNode> _nodes = new();
        private FlowchartNode? _currentNode;

        public FirstAidPage(SurvivalService survivalService)
        {
            InitializeComponent();
            _survivalService = survivalService;
            LoadFlowchart();
        }

        protected override void OnAppearing()
        {
            base.OnAppearing();
            ResetFlowchart();
        }

        private void LoadFlowchart()
        {
            _nodes = _survivalService.GetFirstAidFlowchart();
        }

        private void ResetFlowchart()
        {
            _currentNode = _nodes.FirstOrDefault(n => n.Id == "root");
            UpdateUI();
        }

        private void UpdateUI()
        {
            if (_currentNode == null) return;

            if (_currentNode.IsDecision)
            {
                FlowTextLabel.Text = _currentNode.QuestionText;
                QuestionButtonGrid.IsVisible = true;
                RestartButton.IsVisible = false;
            }
            else
            {
                FlowTextLabel.Text = _currentNode.AdviceText;
                QuestionButtonGrid.IsVisible = false;
                RestartButton.IsVisible = true;
            }
        }

        private void OnYesClicked(object sender, EventArgs e)
        {
            if (_currentNode != null && !string.IsNullOrEmpty(_currentNode.YesNodeId))
            {
                _currentNode = _nodes.FirstOrDefault(n => n.Id == _currentNode.YesNodeId);
                UpdateUI();
            }
        }

        private void OnNoClicked(object sender, EventArgs e)
        {
            if (_currentNode != null && !string.IsNullOrEmpty(_currentNode.NoNodeId))
            {
                _currentNode = _nodes.FirstOrDefault(n => n.Id == _currentNode.NoNodeId);
                UpdateUI();
            }
        }

        private void OnRestartClicked(object sender, EventArgs e)
        {
            ResetFlowchart();
        }
    }
}
