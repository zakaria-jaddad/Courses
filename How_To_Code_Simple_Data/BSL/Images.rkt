;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname Images) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
(require 2htdp/image)
(overlay(circle 20 "solid" "red")
        (circle 30 "solid" "green")
        (circle 40 "solid" "blue")
        (circle 50 "solid" "white"))


(overlay/align "left" "center" (rotate -225 (right-triangle 60 60 "solid" "red")) (above (rectangle 160 30 "solid" "black") (rectangle 160 30 "solid" "white") (rectangle 160 30 "solid" "seagreen")))