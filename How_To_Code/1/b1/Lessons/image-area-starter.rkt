;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname image-area-starter) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))

;; image-area-starter.rkt
(require 2htdp/image)

; 
; PROBLEM:
; 
; DESIGN a function called image-area that consumes an image and produces the 
; area of that image. For the area it is sufficient to just multiple the image's 
; width by its height.  Follow the HtDF recipe and leave behind commented 
; out versions of the stub and template.
; 


;; Image -> Natural

; Natural are number 1 2 3 ...
; Image are sized in pixels so function output won't ever bee a floating point number 

;; produce the area of the given image

;(define (image-area image) 0)   ; Slub

; Examples
(check-expect (image-area (square 10 "solid" "blue")) 100)
(check-expect (image-area (rectangle 10 20 "solid" "blue")) 200)
(check-expect (image-area (rectangle 50 30 "solid" "blue")) (* 50 30))

;(define (image-area image)     ; Template
;  (... image)
;  )


(define (image-area image)
  (* (image-height image) (image-width image))
 )


