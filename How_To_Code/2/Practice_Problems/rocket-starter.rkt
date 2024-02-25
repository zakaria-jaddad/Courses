;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname rocket-starter) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))

;; rocket-starter.rkt

;; =================
;; Data definitions: Itemization

; 
; PROBLEM A:
; 
; You are designing a program to track a rocket's journey as it descends 
; 100 kilometers to Earth. You are only interested in the descent from 
; 100 kilometers to touchdown. Once the rocket has landed it is done.
; 
; Design a data definition to represent the rocket's remaining descent. 
; Call it RocketDescent.
; 


;; RocketDescent is one of
;; - Number[0, 100]
;; - false
;; Interp.
;; - false if rocket landed
;;  - Number between 0 to 100 represent how far is the rocket to tuchdown the Earth

(define R1 1)
(define R2 100)
(define R3 0.5)
(define R4 false)

#;
(define (fn-for-rocket-descent r)
  (cond [(false? r) (...)]
        [else (... r)])
  )

;; Template rules used
;; RocketDescent is one of:
;; - atomic Non-distinct Number[0, 100]
;; - atomic distinc false

;; =================
;; Functions:

; 
; PROBLEM B:
; 
; Design a function that will output the rocket's remaining descent distance 
; in a short string that can be broadcast on Twitter. 
; When the descent is over, the message should be "The rocket has landed!".
; Call your function rocket-descent-to-msg.
; 



;; RocketDescent -> String
;; Porpuse the remaining descent distance of the rocket, if the descent is over porpuse a message


(check-expect (rocket-descent-to-msg 10) (number->string 10))
(check-expect (rocket-descent-to-msg 100) (number->string 100))
(check-expect (rocket-descent-to-msg 0.5) (number->string 0.5))
(check-expect (rocket-descent-to-msg false) "The rocket has landed!")


;(define (rocket-descent-to-msg r) (number->string 10))  ;stub

;; <Template used from RocketDescent>
(define (rocket-descent-to-msg r)
  (cond [(and (number? r) (< 0 r) (<= r 100)) (number->string r)]
        [else "The rocket has landed!"])
  )
