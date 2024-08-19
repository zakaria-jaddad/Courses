;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname area-starter) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))

;; area-starter.rkt

; 
; PROBLEM:
; 
; DESIGN a function called area that consumes the length of one side 
; of a square and produces the area of the square.
; 
; Remember, when we say DESIGN, we mean follow the recipe.
; 
; Leave behind commented out versions of the stub and template.
; 


;; Number -> Number
;; gets length of one side of a square, gives area of it

;(define (area square_side) 0)    ; Slub

(check-expect (area 10) 100)
(check-expect (area 1) 1)
(check-expect (area 20.3) (* 20.3 20.3))

;(define (area square_side)        ; Template
; (... square_side)
;  )

(define (area square_side)         ; Body
  (* square_side square_side)
 )




