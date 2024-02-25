;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname boxify-starter) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
(require 2htdp/image)

;; boxify-starter.rkt

; 
; PROBLEM:
; 
; Use the How to Design Functions (HtDF) recipe to design a function that consumes an image, 
; and appears to put a box around it. Note that you can do this by creating an "outline" 
; rectangle that is bigger than the image, and then using overlay to put it on top of the image. 
; For example:
; 
; (boxify (ellipse 60 30 "solid" "red")) should produce .
; 
; Remember, when we say DESIGN, we mean follow the recipe.
; 
; Leave behind commented out versions of the stub and template.
; 


;; Image -> Image

;; put a box around the given image

(check-expect (boxify (circle 10 "solid" "red"))
              (overlay (circle 10 "solid" "red") (rectangle 22 22 "solid" "white")
                       ))

(check-expect (boxify (circle 20 "solid" "blue"))
              (overlay (circle 20 "solid" "blue") (rectangle 42 42 "solid" "white")))

(check-expect (boxify (square 20 "solid" "blue"))
              (overlay (square 20 "solid" "blue") (rectangle 22 22 "solid" "white")))

;(define (boxify img) (square 10 "solid" "red"))   ; slub

#; 
(define (boxify img)
  (... img)
  )

(define (boxify img)
  (overlay img (rectangle (+ (image-height img) 2) (+ (image-width img) 2) "solid" "white"))
  )



