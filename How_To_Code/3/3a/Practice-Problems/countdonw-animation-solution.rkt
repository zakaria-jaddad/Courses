;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname countdonw-animation-solution) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
(require 2htdp/image)
(require 2htdp/universe)

;; countdown-animation starter.rkt

; 
; PROBLEM:
; 
; Design an animation of a simple countdown. 
; 
; Your program should display a simple countdown, that starts at ten, and
; decreases by one each clock tick until it reaches zero, and stays there.
; 
; To make your countdown progress at a reasonable speed, you can use the 
; rate option to on-tick. If you say, for example, 
; (on-tick advance-countdown 1) then big-bang will wait 1 second between 
; calls to advance-countdown.
; 
; Remember to follow the HtDW recipe! Be sure to do a proper domain 
; analysis before starting to work on the code file.
; 
; Once you are finished the simple version of the program, you can improve
; it by reseting the countdown to ten when you press the spacebar.
; 




;; Countdown timer form 10 to 0

;; =================
;; Constants:

(define TEXT-COLOR "black")
(define TEXT-SIZE       30)
(define WIDTH  300)
(define HEIGHT 300)
(define TEXT-X (/ WIDTH  2))
(define TEXT-Y (/ HEIGHT 2))
(define MTS (empty-scene WIDTH HEIGHT))



;; =================
;; Data definitions:
;; =================

;; CountDown is Natural
;; Interp. current number of Countdown timer
(define CD1 10)
(define CD2  0)

;; Template rules used
;; - atomic non-distinct: Natural
#;
(define (fn-for-countdown c)
  (... c)
  )

;; ====================
;; Function definitions:
;; ====================


;; CountDown -> CountDown
;; start the world with (main 10)
(define (main c)
  (big-bang c                   ; CountDown
    (on-tick advance-countdown 1) ; CountDown -> CountDown
    (to-draw show-countdown)    ; CountDown -> Image
    )
  )


;; Signatur
;; CountDown -> CountDown

;; Porpuse
;; decrement count down number by one

;; Stub
#;
(define (advance-countdown c) 0)

;; Tests
(check-expect (advance-countdown 0) 0)
(check-expect (advance-countdown 10) 9)

;; <used template from CountDown>
(define (advance-countdown c)
  (cond [(> c 0) (- c 1)]
        [else 0])
  )


;; Signature
;; CountDown -> Image

;; Porpuse
;; show an image of the current countdown

;; Stub
#;
(define (show-countdown c)
  (place-image
   (triangle 32 "solid" "red")
   TEXT-X
   TEXT-Y
   MTS
   )
  )

;; Tests
(check-expect (show-countdown 10)
                (place-image
                 (text (number->string 10) TEXT-SIZE TEXT-COLOR)
                 TEXT-X
                 TEXT-Y
                 MTS
                 )
              )
(check-expect (show-countdown 0)
                (place-image
                 (text (number->string 0) TEXT-SIZE TEXT-COLOR)
                 TEXT-X
                 TEXT-Y
                 MTS
                 )
              )

;; <Template rules used CountDown>
(define (show-countdown c)
  (place-image
   (text (number->string c) TEXT-SIZE TEXT-COLOR)
   TEXT-X
   TEXT-Y
   MTS
   )
  )

;; Run
(main 100)


