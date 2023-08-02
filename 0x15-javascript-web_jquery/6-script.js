#!/usr/bin/node
// Script that updates the text color of the <header> element to New Header!!! when the user clicks on <div#update_header>
$('DIV#update_header').click(function () {
    $('header').text('New Header!!!');
    }
);
