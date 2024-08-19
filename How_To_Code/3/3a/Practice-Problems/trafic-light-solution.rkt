;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname traffic-light-solution) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
(require 2htdp/image)
(require 2htdp/universe)

;; traffic-light-starter.rkt

; 
; PROBLEM:
; 
; Design an animation of a traffic light. 
; 
; Your program should show a traffic light that is red, then green, 
; then yellow, then red etc. For this program, your changing world 
; state data definition should be an enumeration.
; 
; Here is what your program might look like if the initial world 
; state was the red traffic light:
; .
; Next:
; .
; Next:
; .
; Next is red, and so on.
; 
; To make your lights change at a reasonable speed, you can use the 
; rate option to on-tick. If you say, for example, (on-tick next-color 1) 
; then big-bang will wait 1 second between calls to next-color.
; 
; Remember to follow the HtDW recipe! Be sure to do a proper domain 
; analysis before starting to work on the code file.
; 
; Note: If you want to design a slightly simpler version of the program,
; you can modify it to display a single circle that changes color, rather
; than three stacked circles. 
; 



; Traffic light that has 3 states red yellow green 

;; =================
;; Constants:
(define RADIUS 30)
(define WIDTH  300)
(define HEIGHT 300)
(define MIDDLE-WIDTH (/ WIDTH  2))
(define MIDDLE-HEIGHT (/ HEIGHT 2))
(define MTS (empty-scene WIDTH HEIGHT "black"))


;; ====================
;; Data definitions:
;; ====================

;; TrafficLight is String
;; Interp. values of trfic light colors

;; Examples
(define TL1 "red")
(define TL2 "yellow")
(define TL3 "green")

#;
(define (fn-for-traffic-light tl)
  (cond [(string=? "red"    tl) (... tl)]
        [(string=? "yellow" tl) (... tl)]
        [else (... tl)])
  )
;; Template rules used
;; atomic distinc
;; - "red": String
;; - "yellow": String
;; - "green": String

;; ====================
;; Function definitions:
;; ====================

(define (main tl)  
  (big-bang tl                                    ; TrafficLight
      (on-tick advance-traffic-light 1)            ; TrafficLight -> TrafficLight 
      (to-draw show-traffic-light)                  ; TrafficLight -> Image         
      )
  )



;; TrafficLight -> TrafficLight
;; advance to next traffic light

;; Stub
#;
(define (advance-traffic-light tl) "red")

;; Test
(check-expect (advance-traffic-light "red") "green")
(check-expect (advance-traffic-light "yellow") "red")
(check-expect (advance-traffic-light "green") "yellow")

;; Template used from TrafficLight
(define (advance-traffic-light tl)
  (cond [(string=? "red"    tl) "green"]
        [(string=? "yellow" tl) "red"]
        [else "yellow"])
  )



;; TrafficLight -> Image
;; show current traffic light from the given state of it

;; Stub
#;
(define (advance-show-traffic-light tl) "hello")

;; Test
(check-expect (show-traffic-light "red")
              (show-image
               (above
                (circle RADIUS "outline" "red")
                (circle RADIUS "outline" "yellow")
                (circle RADIUS "solid" "green")
                )
               )
              )
(check-expect (show-traffic-light "yellow")
              (show-image
               (above
                (circle RADIUS "solid" "red")
                (circle RADIUS "outline" "yellow")
                (circle RADIUS "outline" "green")
                )
               )
              )
(check-expect (show-traffic-light "green")
              (show-image
               (above
                (circle RADIUS "outline" "red")
                (circle RADIUS "solid" "yellow")
                (circle RADIUS "outline" "green")
                )
               )
              )

;; Template used from TrafficLight
(define (show-traffic-light tl)
  (cond [
         (string=? "red" tl)
         (show-image
          (above
           (circle RADIUS "outline" "red")
           (circle RADIUS "outline" "yellow")
           (circle RADIUS "solid" "green")
           )
          )
         ]
        [
         (string=? "yellow" tl)
         (show-image
          (above
           (circle RADIUS "solid" "red")
           (circle RADIUS "outline" "yellow")
           (circle RADIUS "outline" "green")
           )
          )
        
         ]
        [
         else
         (show-image
          (above
           (circle RADIUS "outline" "red")
           (circle RADIUS "solid" "yellow")
           (circle RADIUS "outline" "green")
           )
          )
         ])
  )


;;Image -> Image
;; show image of rafic light in a screen with a given height and width

;;Test
(check-expect (show-image (square 50 "solid" "green"))
              (place-image
               (square 50 "solid" "green")
               MIDDLE-HEIGHT
               MIDDLE-WIDTH
               MTS
              )
              )

;; Template
(define (show-image IMG)
  (place-image IMG MIDDLE-HEIGHT MIDDLE-WIDTH MTS)
  )


;; Run
(main "red")
