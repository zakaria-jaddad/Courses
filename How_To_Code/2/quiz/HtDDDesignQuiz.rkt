;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname HtDDDesignQuiz) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
;; HtDD Design Quiz

;; Age is Natural
;; interp. the age of a person in years
(define A0 18)
(define A1 25)

#;
(define (fn-for-age a)
  (... a))

;; Template rules used:
;; - atomic non-distinct: Natural


; Problem 1:
; 
; Consider the above data definition for the age of a person.
; 
; Design a function called teenager? that determines whether a person
; of a particular age is a teenager (i.e., between the ages of 13 and 19).


;; Age -> Boolean
;; determan if a particular persone is teenager or not

(check-expect (is-teenager? 15) true)
(check-expect (is-teenager? 13) true)
(check-expect (is-teenager? 19) true)
(check-expect (is-teenager? 4) false)

;(define (is-teenager a) true)   ;stub

;; <Template used from Age>
(define (is-teenager? a)
  (and (>= a 13) (<= a 19)))


; Problem 2:
; 
; Design a data definition called MonthAge to represent a person's age
; in months.



;; MonthAge is Natural
;; Interp. represent persone's age with months

;; Examples
(define AGE1 12)
(define AGE2 150)
(define AGE3 3)

;; Template
(define (fun-for-age age)
  (... age)
  )

;; Template relues used
;; Atomic non-distinct: Natural


; Problem 3:
; 
; Design a function called months-old that takes a person's age in years 
; and yields that person's age in months.
; 


;; Signature
;; Age -> Natural

;; Purpose
;; get an age of a person in years and return it in months.

;; Tests
(check-expect (months-old 50) (* 50 12))
(check-expect (months-old 10) (* 10 12))

; Stub
;(define (months-old age) 50)

;; <Template used from Age>
(define (months-old age)
  (* age 12)
  )


; Problem 4:
; 
; Consider a video game where you need to represent the health of your
; character. The only thing that matters about their health is:
; 
;   - if they are dead (which is shockingly poor health)
;   - if they are alive then they can have 0 or more extra lives
; 
; Design a data definition called Health to represent the health of your
; character.
; 
; Design a function called increase-health that allows you to increase the
; lives of a character.  The function should only increase the lives
; of the character if the character is not dead, otherwise the character
; remains dead.


;; =================
;; Data definition:
;; =================

;; CharacterHealth is one of
;; - false
;; - Natural
;; Interp. false means the player is dead, Natural number of lives player has

(define HEALTH1 10)
(define HEALTH3 false)

;; Template rules used
;; - atomic non-distinc: Natural
;; - atomci distinc: false
#;
(define (fun-for-health hp)
  (cond [(number? hp) (... hp)]
        [else (...)]))

;; =================
;; Function definition:
;; =================

;; Signature:
;; CharacterHealth -> Boolean

;; Porpuse
;; return true if the character is alive to increase the live of it,
;; return false if the player is dead

;; Stub
#;
(define (increase-health 50) true)

;; Test/Examples
(check-expect (increase-health 50) true)
(check-expect (increase-health 10) true)
(check-expect (increase-health false) false)


;; <Template used from CharacterHealth>
;; Template rules used
;; one of 2 cases 
;; - atomic not-distinct Natural
;; - atomic distinct false

(define (increase-health hp)
  (cond [(number? hp) true]
        [else false]))






