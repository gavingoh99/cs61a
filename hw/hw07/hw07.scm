(define (cadr s) (car (cdr s)))

(define (caddr s) (car (cdr (cdr s))))

; derive returns the derivative of EXPR with respect to VAR
(define (derive expr var)
  (cond 
    ((number? expr)
     0)
    ((variable? expr)
     (if (same-variable? expr var)
         1
         0))
    ((sum? expr)
     (derive-sum expr var))
    ((product? expr)
     (derive-product expr var))
    ((exp? expr)
     (derive-exp expr var))
    (else
     'Error)))

; Variables are represented as symbols
(define (variable? x) (symbol? x))

(define (same-variable? v1 v2)
  (and (variable? v1) (variable? v2) (eq? v1 v2)))

; Numbers are compared with =
(define (=number? expr num)
  (and (number? expr) (= expr num)))

; Sums are represented as lists that start with +.
(define (make-sum a1 a2)
  (cond 
    ((=number? a1 0)                 a2)
    ((=number? a2 0)                 a1)
    ((and (number? a1) (number? a2)) (+ a1 a2))
    (else                            (list '+ a1 a2))))

(define (make-diff a1 a2)
  (cond 
    ((=number? a1 0)                 a2)
    ((=number? a2 0)                 a1)
    ((and (number? a1) (number? a2)) (- a1 a2))
    (else                            (list '- a1 a2))))

(define (sum? x) (and (list? x) (eq? (car x) '+)))

(define (diff? x) (and (list? x) (eq? (car x) '-)))

(define (first-operand s) (cadr s))

(define (second-operand s) (caddr s))

; Products are represented as lists that start with *.
(define (make-product m1 m2)
  (cond 
    ((or (=number? m1 0) (=number? m2 0))
     0)
    ((=number? m1 1)
     m2)
    ((=number? m2 1)
     m1)
    ((and (number? m1) (number? m2))
     (* m1 m2))
    (else
     (list '* m1 m2))))

(define (product? x)
  (and (list? x) (eq? (car x) '*)))

; You can access the operands from the expressions with
; first-operand and second-operand
(define (first-operand p) (cadr p))

(define (second-operand p) (caddr p))

(define (derive-sum expr var)
  ; differentiates a sum by summing the derivatives of first-operand and second-operand
  (make-sum (derive (first-operand expr) var)
            (derive (second-operand expr) var)))

(define (derive-product expr var)
  ; differentiate a product by summing the product of derivative of first-operand and second-operand
  ; with product of derivative of second-operand and first-operand
  ;if expression is a product of two exponents and they are of the same variable, compute the new expression using laws of indices then pass the new exponent to derive-exp
  (if (and (exp? (first-operand expr))
           (exp? (second-operand expr))
           (same-variable?
            (first-operand (first-operand expr))
            (first-operand (second-operand expr))))
      (derive-exp (make-exp (first-operand (first-operand expr))
                (make-sum (second-operand (first-operand expr))
                    (second-operand (second-operand expr))))
                  var)
      (make-sum
       (make-product (derive (first-operand expr) var)
                     (second-operand expr))
       (make-product (derive (second-operand expr) var)
                     (first-operand expr)))))

; Exponentiations are represented as lists that start with ^.
(define (make-exp base exponent)
  (cond 
    ((=number? exponent 0)
     1)
    ((=number? exponent 1)
     base)
    ((and (number? base) (number? exponent))
     (expt base exponent))
    (else
     (list '^ base exponent))))

(define (exp? exp)
  (and (list? exp) (eq? (car exp) '^)))

(define x^2 (make-exp 'x 2))

(define x^3 (make-exp 'x 3))

(define (derive-exp exp var) 
  ; nested exponentials such as (^ (^ x 3) 2) we can evaluate them first..
  ; differentiate an exponent by taking the product of the exponent and the base with exponent - 1
  (if (exp? (first-operand exp)) ;check if first operand is itself an exponent
      (if (and (variable? (first-operand (first-operand exp))) (variable? (second-operand (first-operand exp)))) ;if first operand contains two diff Variables
          ;chain rule
          (make-product (second-operand exp) (make-exp (first-operand (first-operand exp)) (make-diff (make-exp (second-operand (first-operand exp)) (second-operand exp)) 1)))
      ;else exponent could be nested and same variable we apply indices rule to compute the new exponent then we return derive-exp on the new expression
      ((define exp
        (make-exp (first-operand (first-operand exp))
                        (make-sum (second-operand (first-operand exp))
                                  (second-operand exp))))
                              (derive-exp exp var)))
       ;base case for simple exponent
       (make-product (second-operand exp)
                (make-exp (first-operand exp)
                          (- (second-operand exp) 1)))))
    

