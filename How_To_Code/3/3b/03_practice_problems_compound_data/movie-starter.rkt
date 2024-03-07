;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname movie-starter) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))

;; movie-starter.rkt

;; =================
;; Data definitions:

; 
; PROBLEM A:
; 
; Design a data definition to represent a movie, including  
; title, budget, and year released.
; 
; To help you to create some examples, find some interesting movie facts below: 
; "Titanic" - budget: 200000000 released: 1997
; "Avatar" - budget: 237000000 released: 2009
; "The Avengers" - budget: 220000000 released: 2012
; 
; However, feel free to resarch more on your own!
; 


(define-struct movie (title budget year-released))
;; Movie is (make-movie String Number Number)
;; Intrpe. (make-movie title budget year-relased)
;; - title is title of the movie
;; - budget is the budget of the movie
;; - year-releaser is the realase date of the movie

(define M1 (make-movie "Titanic" 200000000 1997))
(define M2 (make-movie "Avatar" 237000000 2009))

#;
(define (fn-for-movie m)
  (...
   (movie-title m)
   (movie-budget m)
   (movie-year-released m)
   )
  )
;; Templete rules used
;; - cmpound 3 fields

;; =================
;; Functions:

; 
; PROBLEM B:
; 
; You have a list of movies you want to watch, but you like to watch your 
; rentals in chronological order. Design a function that consumes two movies 
; and produces the title of the most recently released movie.
; 
; Note that the rule for templating a function that consumes two compound data 
; parameters is for the template to include all the selectors for both 
; parameters.
; 



;; Movie, Movie -> Movie
;; gets 2 movies and return the most recently released movie

;; Stub
#;
(define (chronological-movie m1 m2) m2)

;; Test
(check-expect (chronological-movie M1 M2) (movie-title M2))
(check-expect (chronological-movie M2 M2) (movie-title M2))

;; Template rules used
(define (chronological-movie m1 m2)
  (if (> (movie-year-released m1) (movie-year-released m2))
      (movie-title m1)
      (movie-title m2)
      )
  )






