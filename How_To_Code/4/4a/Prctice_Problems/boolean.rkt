;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname boolean) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))

;; boolean-list-starter.rkt

;; =================
;; Data definitions:

; 
; PROBLEM A:
; 
; Design a data definition to represent a list of booleans. Call it ListOfBoolean. 
; 

;; ListOfBoolean is one of:
;; - emtpy
;; - (cons Boolean ListOfBoolean)
;; Interp. a list of Booleans
(define LOB1 empty)
(define LOB2 (cons true empty))
(define LOB3 (cons false (cons true empty)))

#;
(define (fn-for-lon lon)
  (cond [(empty? lon) (...)]
        [else
         (... (first lon)
              (fn-for-lon (rest lon)))]))

;; Templete rules used:
;; - one of 2 cases
;; - atomic distinct: empty
;; - self refrence (rest lob) is ListOfBoolean


;; =================
;; Functions:

; 
; PROBLEM B:
; 
; Design a function that consumes a list of boolean values and produces true 
; if every value in the list is true. If the list is empty, your function 
; should also produce true. Call it all-true?
; 


;; listOfBoolean -> listOfBoolean
;; produce true if all items in list are true, if list is empty produce true
(check-expect (all-true? LOB1) true)
(check-expect (all-true? LOB2) true)
(check-expect (all-true? LOB3) false)
(check-expect (all-true? empty) true)
(check-expect (all-true? (cons true (cons true (cons true (cons true empty))))) true)

;(define (all-true lob) true) ;stub


(define (all-true? lon)
  (cond [(empty? lon) true]
        [else
         (if (false? (first lon))
             false
             (all-true? (rest lon)))]))



