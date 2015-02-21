console.log('index');

$(function() {

    $.get('data/disclosures.json',
          function(data) {
              console.log(data);
              $('body').append($('<p>').text(JSON.stringify(data)));
          });
});
