odoo.define("login_layout.cidsdes1", function (require) {
    var ajax = require("web.ajax");
    var core = require('web.core');

  $(document).ready(function() {
  console.log("ready");
$(".toggle-password").click(function() {

  $(this).toggleClass("fa-eye fa-eye-slash");
  var input = $($(this).attr("toggle"));
  if (input.attr("type") == "password") {
    input.attr("type", "text");
  } else {
    input.attr("type", "password");
  }
});
   })


   $(document).ready(function() {
  console.log("ready1112");
$(".toggle-passwordconf").click(function() {
  $(this).toggleClass("fa-eye fa-eye-slash");
  var input = $($(this).attr("toggle"));
  if (input.attr("type") == "password") {
    input.attr("type", "text");
  } else {
    input.attr("type", "password");
  }
});
   })

    });