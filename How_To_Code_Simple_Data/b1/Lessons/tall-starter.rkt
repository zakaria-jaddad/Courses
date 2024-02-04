;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname tall-starter) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
(require 2htdp/image)
;; tall-starter.rkt

; 
; PROBLEM:
; 
; DESIGN a function that consumes an image and determines whether the 
; image is tall.
; 
; Remember, when we say DESIGN, we mean follow the recipe.
; 
; Leave behind commented out versions of the stub and template.
; 


;; Image -> Boolean
;; preduce true if the image is tall, false other wise 
(check-expect (is-image-tall? (rectangle 20 10 "solid" "red")) false) ; height less image not tall 
(check-expect (is-image-tall? (rectangle 5 10 "solid" "red")) true)   ; height greaterimage is tall 
(check-expect (is-image-tall? (rectangle 5 5 "solid" "red")) false)   ; height = width image is meh 

;(define (is-image-tall? img) false)   ; Slub

;(define (is-image-tall? img)          ; Template
;  (... img)
; )

; body
(define (is-image-tall? img)
   (> (image-height img) (image-width img))
 )




