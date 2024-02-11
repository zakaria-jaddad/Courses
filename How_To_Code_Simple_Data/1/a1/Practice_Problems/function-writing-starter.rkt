;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname function-writing-starter) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))

;; function-writing-starter.rkt

; 
; PROBLEM:
; 
; Write a function that consumes two numbers and produces the larger of the two. 
; 



(define (myFunction x y) 
    (if (> x y) x y)
  )

(myFunction 3 2)
(myFunction 18 2)
(myFunction -30 2)
(myFunction 1 2)
(myFunction 5 2)
(myFunction 0 2)
