(function($) {
  $(function() {
        $('.sidenav').sidenav();
        $('.collapsible').collapsible();
        $('.collapsible.expandable').collapsible({
                accordion: false
        });
  });
})(jQuery); // end of jQuery name space