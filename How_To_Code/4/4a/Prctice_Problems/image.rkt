;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname image) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
(require 2htdp/image)

;; image-list-starter.rkt

;; =================
;; Data definitions:

; 
; PROBLEM A:
; 
; Design a data definition to represent a list of images. Call it ListOfImage. 
; 


;; ListOfImagae is one of:
;; - empty
;; - (cons Image ListOfImages)
;; Iterp. list of Images
(define LOI1 empty)
(define LOI2 (cons (circle 30 "outline" "red") empty))
(define LOI3 (cons (circle 30 "outline" "red")
                   (cons (circle 30 "solid" "gold") empty)))

#;
(define (for-fn-loi loi)
  (cond [(empty? loi) (...)]
  [else
   (... (first loi)
   (fn-for-los (rest loi)))]))

;; Templete rules used:
;; one of 2 cases:
;; atomic distinct: empty
;; atomic non distinct (cons Image ListOfImage)
;; self-reference: (rest loi) is ListOfImages

;; =================
;; Functions:

; 
; PROBLEM B:
; 
; Design a function that consumes a list of images and produces a number 
; that is the sum of the areas of each image. For area, just use the image's 
; width times its height.
; 


;; ListOfImages -> Number
;; produce the sum of the ares of each images given in a list
(check-expect (total-area empty) 0)
(check-expect (total-area LOI1) 0)
(check-expect (total-area LOI2) 3600)
(check-expect (total-area LOI3) (+ 3600 3600))

; (define (total-area loi) 0) ;stub

(define (total-area loi)
  (cond [(empty? loi) 0]
  [else
   (+
    (* (image-width (first loi)) (image-height (first loi)))
    (total-area (rest loi)))]))



