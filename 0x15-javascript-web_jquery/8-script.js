$.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  $.each(data.results, function (i, item) {
    $('#list_movies').append('<li>' + data.results[i].title + '</li>');
    //  alert(data.results[i].title);
  });
});
