;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname countdown-starter) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))

;; countdown-starter.rkt

; 
; PROBLEM:
; 
; Consider designing the system for controlling a New Year's Eve
; display. Design a data definition to represent the current state 
; of the countdown, which falls into one of three categories: 
; 
;  - not yet started
;  - from 10 to 1 seconds before midnight
;  - complete (Happy New Year!)
; 



; Itemisation : is comprised of 2 or more subclasses, at least one of which is not a distinct item

;; CountDown is one of:
;; - false
;; - Natural[1, 10]
;; - complete

;; interp.
;; - false means the countdown not yet started
;; - Natural[1, 10] means countdown is running + how many seconds left 
;; - "complete" means happy new year

;; Eamples
(define CD1 false)
(define CD2 10)
(define CD3 1)
(define CD4 "complete")


#;
(define (fu-for-coundown c)
  (cond [(false? c) (...)]
        [(and (number? c) (<= 1 c) (< c 10)) (... c)]
        [(string=? c (...))])
  )

#;
(define (fu-for-coundown c)
  (cond [(false? c) (...)]
        [(and (number? c) (<= 1 c) (< c 10)) (... c)]
        [else (...)])
  )


(define (fu-for-coundown c)
  (cond [(false? c) (...)]
        [(number? c) (... c)]
        [(string=? c "complete")])
  )
;; Template rules are used
;; one of 3 cases
;; - atomic distinc: false
;; - atomic non-distinc: Natural[1, 10]
;; - atomic distinc: "complete"


