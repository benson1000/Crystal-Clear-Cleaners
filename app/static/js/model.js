$(document).ready(function() {
    $('.nav-link[data-target="#quoteModal"]').click(function(e) {
      e.preventDefault(); // Prevent default link behavior
      $('#quoteModal').modal('show'); // Trigger modal using jQuery modal plugin
    });
  
    $('.modal-content .close').click(function() {
      $('#quoteModal').modal('hide');
    });
  });
  