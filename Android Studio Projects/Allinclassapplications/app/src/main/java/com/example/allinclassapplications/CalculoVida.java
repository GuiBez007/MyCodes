package com.example.allinclassapplications;

import android.app.Activity;
import android.app.DatePickerDialog;
import android.content.BroadcastReceiver;
import android.content.ComponentName;
import android.content.ContentResolver;
import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;
import android.content.IntentSender;
import android.content.ServiceConnection;
import android.content.SharedPreferences;
import android.content.pm.ApplicationInfo;
import android.content.pm.PackageManager;
import android.content.res.AssetManager;
import android.content.res.Configuration;
import android.content.res.Resources;
import android.database.DatabaseErrorHandler;
import android.database.sqlite.SQLiteDatabase;
import android.graphics.Bitmap;
import android.graphics.drawable.Drawable;
import android.net.Uri;
import android.os.Bundle;
import android.os.Handler;
import android.os.Looper;
import android.os.UserHandle;
import android.util.Log;
import android.view.Display;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.time.LocalDate;

public class CalculoVida {
    private static int ano, mes, dia;
    public static TextView nascimento;

    public void configurarDataNascimento(Context context, TextView txtNascimento, OnDateSelectedListener listener) {
        // Get the current date
        LocalDate dataAtual = LocalDate.now();

        ano = dataAtual.getYear();
        mes = dataAtual.getMonthValue();
        dia = dataAtual.getDayOfMonth();

        DatePickerDialog data = new DatePickerDialog(context, (view1, year, month, day) -> {
            // New mode
            String day_, month_, year_;
            day_ = month_ = year_ = "";
            //
            if (day < 10)
                day_ = "0";
            if ((month+1) < 10)
                month_ = "0";

            txtNascimento.setText(day_ + day + "/" + month_ + (month+1) + "/" + year);
            nascimento = txtNascimento;
            listener.onDateSelected(year, month, day);
        }, ano, mes-1, dia);

        data.show();
    }

    public static String calcularTempo() {
        int years, months, days, hours, minutes, seconds;
        years = months = days = hours = minutes = seconds = 0;
        String resultado, aux;

        aux = nascimento.getText().toString().substring(20, 30);
        days = Integer.parseInt(aux.substring(0, 2));
        months = Integer.parseInt(aux.substring(3, 5));
        years = Integer.parseInt(aux.substring(6, 10));

        // Subtract of txtNascimento by actual date
        LocalDate data1 = LocalDate.of(years, months, days);
        LocalDate data2 = LocalDate.of(ano, mes, dia);

        days = data1.until(data2).getDays();
        months = data1.until(data2).getMonths();
        years = data1.until(data2).getYears();
        resultado = years + " anos\n";

        months += (years * 12);
        resultado += months + " meses\n";

        days += (months * 30);
        resultado += days + " dias\n";

        hours += (days * 24);
        resultado += hours + " horas\n";

        minutes += (hours * 60);
        resultado += minutes + " minutos\n";

        seconds += (minutes * 60);
        resultado += seconds + " segundos";

        return resultado;
    }

}
