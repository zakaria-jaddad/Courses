;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname demolish-starter) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))

;; demolish-starter.rkt

;; =================
;; Data definitions:

; 
; PROBLEM A:
; 
; You are assigned to develop a system that will classify 
; buildings in downtown Vancouver based on how old they are. 
; According to city guidelines, there are three different classification levels:
; new, old, and heritage.
; 
; Design a data definition to represent these classification levels. 
; Call it BuildingStatus.
; 


;; BuildingStatus is one of
;; - "new"
;; - "old"
;; - "heritage"
;; Interp. classification of buildings of Vancouver.

; <Examples are deprecated in Enumeration>

#;
(define (fn-for-building-status building)
  (cond [(string=? building "new") (...)]
        [(string=? building "old") (...)]
        [(string=? building "heritage") (...)])
  )

;; Template rules used
;; one-of 3 cases:
;; - atomic-distinc "new"
;; - atomic-distinc "old"
;; - atomic-distinc "heritage"




;; =================
;; Functions:

; 
; PROBLEM B:
; 
; The city wants to demolish all buildings classified as "old". 
; You are hired to design a function called demolish? 
; that determines whether a building should be torn down or not.
; 


;; BuildingStatus -> Boolean
;; Determines weather the building is old or not

(check-expect (demolish "old") true)
(check-expect (demolish "new") false)
(check-expect (demolish "heritage") false)


;(define (demolish building) true)   ;stub

;; <Template used from BuildingStatu>
(define (demolish building)
  (cond [(string=? building "new") false]   
        [(string=? building "heritage") false]
        [else true])
  )






