;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname if_condition) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
;image manipulation
(require 2htdp/image)


; This is if condition

(if (string=? "foo" "bar")
    "hello There true"
    "hello There false")

;if in images
;                     W  H
(define I1 (rectangle 10 20 "solid" "red"))
(define I2 (rectangle 20 10 "solid" "blue"))

; in this condition i check if the width of th image 2 is greather than it's height
; if so retun it's with value
; if not retun it's height value 

; ouput image I2 height 20px
(if (> (image-width I2) (image-height I2))
    (image-width I2)
    (image-height I2)
   )

; is I1 taller than I2
(> (image-height I1) (image-height I2))

; is I1 thiner than I2
(< (image-width I1) (image-width I2))

; and operator to see if 2 conditions are true and evaluate true or false
; also and uses the short 
(and
 (> (image-height I1) (image-height I2))
 (< (image-width I1) (image-width I2))
 )