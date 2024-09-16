;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname decreassing-image) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
(require 2htdp/image)

;; decreasing-image-starter.rkt

;  PROBLEM:
;  
;  Design a function called decreasing-image that consumes a Natural n and produces an image of all the numbers 
;  from n to 0 side by side. 
;  
;  So (decreasing-image 3) should produce .

(define TEXT-SIZE 20)
(define TEXT-COLOR "black")
(define SPACING (text " " TEXT-SIZE TEXT-COLOR))

;; Natural -> Image
;; produce an image of n, n-1, ... 0 side by side
(check-expect (decreasing-image 0) (text "0" 20 "black"))
(check-expect (decreasing-image 3) (beside (text "3" 20 "black") SPACING 
                                           (text "2" 20 "black") SPACING
                                           (text "1" 20 "black") SPACING
                                           (text "0" 20 "black")))

(define (decreasing-image n)
  (cond [(zero? n) (text "0" 20 "black")]
        [else
         (beside
          (text (number->string n) TEXT-SIZE TEXT-COLOR) SPACING
          (decreasing-image (- n 1))
          )
         ]
  ))