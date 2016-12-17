var TheLongView = angular.module('TheLongView', ['ui.router']);

TheLongView.config(function($stateProvider, $urlRouterProvider) {
  $urlRouterProvider.otherwise('/');
  $urlRouterProvider.when('browse','browse.all');

  var homeState = {
    name: 'home',
    url: '/',
    templateUrl: 'timeline.html'
  }
  var articleState = {
    name: 'article',
    url: '/lorem-ipsum',
    templateUrl: 'articles/lorem-ipsum.html'
  }
  $stateProvider.state(homeState)
        .state(articleState);
});

TheLongView.controller('IndexCtrl', function($scope) {
});
TheLongView.controller('TimelineCtrl', function($scope) {
	$('.target-div').hide();
	$('.show').click(function () {
	    if (! ($(this).hasClass('active'))) {
	    	$('.target-div').hide();
	    	$('#div' + $(this).attr('target')).slideDown();
	    	$('.show').removeClass("active");
	    	$(this).addClass("active");
	    }
	});

	$('.hide').click(function () {
	    $('.target-div').slideUp();
	    $('.show').removeClass("active");
	});
});