angular.module('indexApp', ['indexApp.js.index']);

var indexPage = angular.module("indexApp.js.index", ["firebase"]);

indexPage.controller("transactionTagCtrl", function($scope, $firebaseAuth) {

    /*
    var ref = new Firebase("https://luminous-heat-1383.firebaseio.com");
    // create an instance of the authentication service
    var auth = $firebaseAuth(ref);
    // login with Google
    auth.$authWithOAuthRedirect("google").then(function(authData) {
        console.log("Logged in as:", authData.uid);
    }).catch(function(error) {
        console.log("Authentication failed:", error);
    });
    */

})