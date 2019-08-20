%prueba proyecto
close all
clear ll
n = 100;                            %cantidad de datos
fvar = 0.1;                         %efecto del ruido
m = 8;                              %2,4,8,16,...
r = 5;                              %repeticiones (para comparar entre diferentes señales)

datos = round((m-1)*rand(r,n));     %datos
a1bar = zeros(1,r);
a1var = zeros(1,r);
for i=1:r
    angles = datos(i,:)*2*pi/m;              %fase correspondiente
    envolvente = (fvar*randn(1,n)+1).*exp(1i*(angles+fvar*randn(1,n)));  %envolvente, se agrega efectos aleatorios
    a = real(envolvente);           %parte real
    b = imag(envolvente);           %parte imaginaria

    %constelaciones
    lim = 1.5;
    figure(i)
    scatter(a,b)
    ylim([-lim,lim])
    xlim([-lim,lim])
    grid

    cond1 = (a<1.5 & a>0.5) & abs(b)<0.5;   %encontrar valores alrededor de 1 + j0

    %datos seleccionados
    a1 = a(cond1);
    b1 = b(cond1);

    figure(i+r)
    scatter(a1,b1)
    ylim([-lim,lim])
    xlim([-lim,lim])
    grid
    a1bar(i) = sum(a1)/size(a1,2);
    a1var(i) = sum((a1 - a1bar(i)).^2)/(size(a1,2)-1);
end

find(a1var==min(a1var))   %señal mas adecuada

