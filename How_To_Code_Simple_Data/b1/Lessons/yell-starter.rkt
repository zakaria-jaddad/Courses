;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname yell-starter) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))

;; yell-starter.rkt

; 
; PROBLEM:
; 
; DESIGN a function called yell that consumes strings like "hello" 
; and adds "!" to produce strings like "hello!".
; 
; Remember, when we say DESIGN, we mean follow the recipe.
; 
; Leave behind commented out versions of the stub and template.
; 


; Signature
;; String -> String

; Purpose
;; add ! to the given string plus 

; (define (yell str) "") ; Slub

; Examples 
(check-expect (yell "hello") (string-append "hello" "!"))
(check-expect (yell "Hello, World") "Hello, World!")
(check-expect (yell "Hello, World!") "Hello, World!!")


; Template
;(define (yell str)
;  (... str)
;) 

; Body
(define (yell str)
  (string-append str "!")
  )








