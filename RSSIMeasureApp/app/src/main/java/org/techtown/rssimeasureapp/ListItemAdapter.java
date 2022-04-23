package org.techtown.rssimeasureapp;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.TextView;

import java.util.ArrayList;

public class ListItemAdapter extends BaseAdapter {
    ArrayList<String> device = new ArrayList<String>();
    ArrayList<String> address = new ArrayList<String>(); // each devices are distinguished by its MAC address.
    ArrayList<String> rssi = new ArrayList<String>();
    ArrayList<String> rssiKalman = new ArrayList<String>();
    ArrayList<String> distance = new ArrayList<String>();
    Context context;

    @Override
    public int getCount() {
        return address.size();
    }

    @Override
    public Object getItem(int i) {
        return address.get(i);
    }

    @Override
    public long getItemId(int i) {
        return i;
    }

    @Override
    public View getView(int position, View convertView, ViewGroup parent) {
        context = parent.getContext();

        if(convertView == null){
            LayoutInflater inflater = (LayoutInflater)context.getSystemService(Context.LAYOUT_INFLATER_SERVICE);
            convertView = inflater.inflate(R.layout.listview_item, parent, false);
        }

        TextView deviceText = convertView.findViewById(R.id.device);
        TextView addressText = convertView.findViewById(R.id.address);
        TextView rssiText = convertView.findViewById(R.id.rssi);

        deviceText.setText(this.device.get(position));
        addressText.setText(this.address.get(position));
        rssiText.setText(this.rssi.get(position) + " / filtered : " + this.rssiKalman.get(position));

        return convertView;
    }

    public void addItem(String device, String address, String rssi, String rssiKalman){
        this.device.add(device);
        this.address.add(address);
        this.rssi.add(rssi);
        this.rssiKalman.add(rssiKalman);
        this.distance.add("" + Triangulation.RssiToDistance(Integer.parseInt(rssi)));
    }
    public void setItem(String device, String address, String rssi, String rssiKalman, int index){
        this.device.set(index, device);
        this.address.set(index, address);
        this.rssi.set(index, rssi);
        this.rssiKalman.set(index, rssiKalman);
        this.distance.set(index, "" + Triangulation.RssiToDistance(Integer.parseInt(rssi)));
    }
}
